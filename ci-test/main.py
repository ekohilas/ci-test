import sys

import gitlab_ci_local_parser
import rule_collator
import rule_printer


def main(json_path: str):
    jsonParser = gitlab_ci_local_parser.JsonParser(
        json_path=json_path,
    )
    jobs = jsonParser.get_jobs()
    ruleCollator = rule_collator.RuleCollator(
        ci_jobs=jobs,
    )
    jobs_by_rules = ruleCollator.jobs_by_rules()
    rulePrinter = rule_printer.RulePrinter(
        collated_rules=jobs_by_rules,
    )
    rulePrinter.print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_json>")
        sys.exit(1)

    json_path = sys.argv[1]
    main(json_path=json_path)
