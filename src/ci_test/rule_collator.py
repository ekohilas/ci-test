import collections

from ci_test import job_rules


class RuleCollator:
    def __init__(self, ci_jobs: list[job_rules.CiJob]):
        self.ci_jobs = ci_jobs

    def jobs_by_rules(self) -> dict[job_rules.Rule, set[job_rules.CiJob]]:
        jobs_by_rules = collections.defaultdict(set)
        for job in self.ci_jobs:
            for rule in job.rules:
                jobs_by_rules[rule].add(job)
        return jobs_by_rules


if __name__ == "__main__":
    import gitlab_ci_local_parser
    import sys

    jsonParser = gitlab_ci_local_parser.JsonParser(sys.argv[1])
    jobs = jsonParser.get_jobs()
    ruleCollator = RuleCollator(ci_jobs=jobs)
    jobs_by_rules = ruleCollator.jobs_by_rules()
    import pprint

    pprint.pprint(jobs_by_rules)
