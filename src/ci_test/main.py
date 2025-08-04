import sys

from ci_test import gitlab_ci_local_parser
from ci_test import rule_collator
from ci_test import rule_formatter
from ci_test import flags
import json


def main(json_path: str, option_flags: flags.Flags) -> str:
    jsonParser = gitlab_ci_local_parser.JsonParser(
        json_path=json_path,
    )
    jobs = jsonParser.get_jobs()
    ruleCollator = rule_collator.RuleCollator(
        ci_jobs=jobs,
        option_flags=option_flags,
    )
    jobs_by_rules = ruleCollator.jobs_by_rules()
    ruleFormatter = rule_formatter.RuleFormatter(
        collated_rules=jobs_by_rules,
    )
    formatted_rules = ruleFormatter.format()
    json_output = json.dumps(
        formatted_rules,
        indent=2,
    )
    return json_output
