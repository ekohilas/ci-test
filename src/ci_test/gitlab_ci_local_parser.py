from ci_test import job_rules

import json


class JsonParser(job_rules.JobRulesParser):
    def __init__(self, json_path):
        self.json_path = json_path

    def get_jobs(self) -> list[job_rules.CiJob]:
        json_object = self._parse()
        jobs = tuple(self.parse_job(obj) for obj in json_object)
        return jobs

    def _parse(self) -> list[dict]:
        with open(self.json_path) as f:
            json_object = json.load(f)
        return json_object

    @classmethod
    def parse_job(cls, json_object: dict) -> job_rules.CiJob:
        name = json_object["name"]
        json_rules = json_object.get("rules", [])
        rules = cls.parse_rules(
            json_rules=json_rules,
        )
        job = job_rules.CiJob(
            name=name,
            rules=rules,
        )
        return job

    @classmethod
    def parse_rules(cls, json_rules: list[dict]) -> list[job_rules.Rule]:
        filtered_rules = (
            json_rule for json_rule in json_rules if json_rule != {"when": "never"}
        )
        rules = tuple(cls.parse_rule(json_object) for json_object in filtered_rules)
        return rules

    @classmethod
    def parse_rule(cls, json_rule: dict) -> job_rules.Rule:
        if_rule = (
            job_rules.IfRule(
                condition=json_rule["if"],
            )
            if "if" in json_rule
            else None
        )

        changes_rule = (
            job_rules.ChangesRule(
                changes=tuple(
                    job_rules.GlobPath(glob_path=change)
                    for change in json_rule["changes"]
                )
            )
            if "changes" in json_rule
            else None
        )

        # TODO: Log for other rules

        rule = job_rules.Rule(
            if_rule=if_rule,
            changes_rule=changes_rule,
        )

        return rule


if __name__ == "__main__":
    import sys

    jsonParser = JsonParser(json_path=sys.argv[1])
    jobs = jsonParser.get_jobs()

    import pprint

    pprint.pprint(jobs)
