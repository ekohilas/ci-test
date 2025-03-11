from ci_test import job_rules


class RuleFormatter:
    def __init__(
        self,
        collated_rules: dict[job_rules.Rule, set[job_rules.CiJob]],
    ):
        self.collated_rules = collated_rules

    def format(self):
        json_object = []
        for rule, jobs in self.collated_rules.items():
            rule_dict = {}

            if rule.if_rule:
                rule_dict["if"] = rule.if_rule.condition

            if rule.changes_rule:
                rule_dict["changes"] = sorted(
                    change.glob_path for change in rule.changes_rule.changes
                )

            rule_dict["jobs"] = sorted(job.name for job in jobs)

            json_object.append(rule_dict)

        sorted_json_object = sorted(
            json_object,
            key=lambda x: any(
                (
                    x.get("if"),
                    str(x.get("changes")),
                    str(x["jobs"]),
                )
            ),
        )
        return sorted_json_object


if __name__ == "__main__":
    import gitlab_ci_local_parser
    import sys

    jsonParser = gitlab_ci_local_parser.JsonParser(
        json_path=sys.argv[1],
    )
    jobs = jsonParser.get_jobs()

    import rule_collator

    ruleCollator = rule_collator.RuleCollator(
        ci_jobs=jobs,
    )
    jobs_by_rules = ruleCollator.jobs_by_rules()

    rulePrinter = RuleFormatter(
        collated_rules=jobs_by_rules,
    )
    rulePrinter.format()
