import sys

from ci_test import gitlab_ci_local_parser
from ci_test import rule_collator
from ci_test import rule_formatter
import json


def main(json_path: str):
    jsonParser = gitlab_ci_local_parser.JsonParser(
        json_path=json_path,
    )
    jobs = jsonParser.get_jobs()
    ruleCollator = rule_collator.RuleCollator(
        ci_jobs=jobs,
    )
    jobs_by_rules = ruleCollator.jobs_by_rules()
    ruleFormatter = rule_formatter.RuleFormatter(
        collated_rules=jobs_by_rules,
    )
    formatted_rules = ruleFormatter.format()
    print(
        json.dumps(
            formatted_rules,
            indent=2,
        )
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_json>")
        sys.exit(1)

    json_path = sys.argv[1]
    main(json_path=json_path)
