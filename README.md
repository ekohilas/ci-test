# CI Test
## Evan Kohilas

A framework for static analysis testing of CI configurations.

## Installation

Install using `pipx install ci-test-toolkit` to add `ci-test` to your PATH.

The tool can be run either via `ci-test` once installed or `python -m ci_test` from within the `src` folder.

## Example

`ci-test gitlab rule-snapshot <path_to_json>` will create a snapshot of your ci configuration, by listing all rulesets and the jobs that will run for each of them.

This snapshot can then be used to generate diffs of the linking between jobs and their rules.

## Input Generation

Currently the tool is setup to take input of the following form:

```json
[
    {
        "name": "job-name",
        "rules": [
            {
                "if": "$CI_PIPELINE_SOURCE == 'push'"
            },
            {
                "if": "$CI_PIPELINE_SOURCE == 'merge_request_event'",
                "changes": [
                    "**/*.py"
                ]
            },
        ]
    }
]
```

This is easiest made using [gitlab-ci-local](https://github.com/firecow/gitlab-ci-local)

With `node` installed, run `npx gitlab-ci-local --list-json > gitlab-ci-local.json` in a project directory with a `.gitlab-ci.yml` file.

Then, run `ci-test gitlab rule-snapshot gitlab-ci-local.json` to create a collated snapshot.

## TODO

- Remove the dependency on `gitlab-ci-local`
- Support GitHub configurations
- Add more testing commands
- Add better CLI
- Add linting/formatting
- Clean up for best practices

## Contibuting

Please see `CONTRIBUTING.md` for a head start.

Pull requests welcome!

