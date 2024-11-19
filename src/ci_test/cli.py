import sys

from ci_test import main


def cli():
    try:
        program_name, ci_type, command, json_path, *_ = sys.argv
    except ValueError:
        raise SystemExit(f"Usage: {sys.argv[0]} gitlab rule-snapshot <path_to_json>")

    if ci_type != "gitlab":
        raise SystemExit(f"subcommand {ci_type} is not currently supported")

    if command != "rule-snapshot":
        raise SystemExit(f"subcommand {command} is not currently supported")

    json_output = main.main(json_path=json_path)
    print(json_output)


if __name__ == "__main__":
    cli()
