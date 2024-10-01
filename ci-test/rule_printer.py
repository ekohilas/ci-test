import job_rules


class RulePrinter:
    def __init__(
        self,
        collated_rules: dict[job_rules.Rule, set[job_rules.CiJob]],
    ):
        self.collated_rules = collated_rules

    def print(self):
        for rule, jobs in self.collated_rules.items():
            print(rule)

            for job in jobs:
                print(f"\t{job.name}")

            print()


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

    rulePrinter = RulePrinter(
        collated_rules=jobs_by_rules,
    )
    rulePrinter.print()
