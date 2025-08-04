import sys

from ci_test import main
from ci_test import flags

class Cli:
    cli_string_to_flag = {
        "output-jobs-with-no-rules": flags.Flags.OUTPUT_JOBS_WITH_NO_RULES,
    }

    def __init__(self, args):
        self.args = args

    def process(self):
        try:
            program_name, ci_type, command, json_path, *extra = self.args
        except ValueError:
            raise SystemExit(f"Usage: {self.args[0]} gitlab rule-snapshot <path_to_json>")

        if ci_type != "gitlab":
            raise SystemExit(f"subcommand {ci_type} is not currently supported")

        if command != "rule-snapshot":
            raise SystemExit(f"subcommand {command} is not currently supported")

        cli_flags = Cli.parse_extra_args_as_flags(args=extra)

        json_output = main.main(
            json_path=json_path,
            option_flags=cli_flags,
        )
        print(json_output)

    @staticmethod
    def parse_extra_args_as_flags(args: list[str]) -> flags.Flags:
        cli_flags = flags.Flags.NONE
        for arg in args:
            flag_start = "--flag-"
            if arg.startswith(flag_start):
                flag = arg.removeprefix(flag_start)     
                cli_flags |= Cli.parse_flag(flag)
            else:
                raise SystemExit(f"Unknown argument: {arg}")
        return cli_flags

    @staticmethod
    def parse_flag(flag: str) -> flags.Flags:
        return Cli.cli_string_to_flag[flag]

    @classmethod
    def process_from_sys_argv(cls):
        cli = Cli(sys.argv)
        cli.process()


if __name__ == "__main__":
    Cli.process_from_sys_argv()
