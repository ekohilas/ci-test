from ci_test.job_rules import JobRulesParser
from ci_test.job_rules import CiJob
from ci_test.job_rules import Rule
from ci_test.job_rules import IfRule
from ci_test.job_rules import ChangesRule

import json


class JsonParser(JobRulesParser):
    def __init__(self, json_path):
        self.json_path = json_path

    def get_jobs(self) -> list[CiJob]:
        json_object = self._parse()
        jobs = tuple(self.parse_job(obj) for obj in json_object)
        return jobs

    def _parse(self) -> list[dict]:
        with open(self.json_path) as f:
            json_object = json.load(f)
        return json_object

    @classmethod
    def parse_job(cls, json_object: dict) -> CiJob:
        name = json_object["name"]
        json_rules = json_object.get("rules", [])
        rules = cls.parse_rules(
            json_rules=json_rules,
        )
        job = CiJob(
            name=name,
            rules=rules,
        )
        return job

    @classmethod
    def parse_rules(cls, json_rules: list[dict]) -> list[Rule]:
        filtered_rules = (
            json_rule for json_rule in json_rules if json_rule != {"when": "never"}
        )
        rules = tuple(cls.parse_rule(json_object) for json_object in filtered_rules)
        return rules

    @classmethod
    def parse_rule(cls, json_rule: dict) -> Rule:
        if_rule = (
            IfRule(
                condition=json_rule["if"],
            )
            if "if" in json_rule
            else None
        )

        changes_rule = (
            ChangesRule(
                changes=tuple(
                    GlobPath(glob_path=change)
                    for change in json_rule["changes"]
                )
            )
            if "changes" in json_rule
            else None
        )

        # TODO: Log for other rules

        rule = Rule(
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
