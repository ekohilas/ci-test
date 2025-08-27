from ci_test import job_rules
from ci_test.rule_sorter import RuleSorter


class RuleFormatter:
    def __init__(
        self,
        collated_rules: dict[job_rules.Rule, set[job_rules.CiJob]],
        rule_sorter: RuleSorter,
    ):
        self.collated_rules = collated_rules
        self.rule_sorter = rule_sorter

    def format(self):
        json_object = []
        for rule, jobs in self.collated_rules.items():
            # TODO: Update type
            rule_dict = {}

            if rule.if_rule:
                rule_dict["if"] = rule.if_rule.condition

            if rule.changes_rule:
                rule_dict["changes"] = sorted(
                    change.glob_path for change in rule.changes_rule.changes
                )

            rule_dict["jobs"] = sorted(job.name for job in jobs)

            json_object.append(rule_dict)

        sort_function = self.rule_sorter.sort_function

        sorted_json_object = sorted(
            json_object,
            key=sort_function,
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

    import rule_sorter

    ruleSorter = rule_sorter.RuleSorter()

    rulePrinter = RuleFormatter(
        collated_rules=jobs_by_rules,
        rule_sorter=ruleSorter,
    )
    rulePrinter.format()
