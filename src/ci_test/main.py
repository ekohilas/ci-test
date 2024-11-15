import sys

from ci_test.gitlab_ci_local_parser import JsonParser
from ci_test.rule_collator import RuleCollator
from ci_test.rule_formatter import RuleFormatter
import json


def main(json_path: str):
    jsonParser = JsonParser(
        json_path=json_path,
    )
    jobs = jsonParser.get_jobs()
    ruleCollator = RuleCollator(
        ci_jobs=jobs,
    )
    jobs_by_rules = ruleCollator.jobs_by_rules()
    ruleFormatter = RuleFormatter(
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
