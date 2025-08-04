import unittest


from ci_test import flags
from ci_test import main


class MainIntegrationTest(unittest.TestCase):
    def test_main_returns_expected_output(self):
        input_path = "test/input.json"
        actual_output = main.main(input_path, option_flags=flags.Flags.NONE)

        expected_output_path = "test/output.json"

        with open(expected_output_path) as f:
            expected_output = f.read()

        self.assertEqual(actual_output, expected_output)

    def test_input_job_with_no_rules_outputs_job_when_given_flag(self):
        input_path = "test/job_no_rules_input.json"
        actual_output = main.main(input_path, option_flags=flags.Flags.OUTPUT_JOBS_WITH_NO_RULES)

        expected_output_path = "test/job_no_rules_output.json"

        with open(expected_output_path) as f:
            expected_output = f.read()

        self.assertEqual(actual_output, expected_output)

    def test_input_job_with_no_rules_outputs_nothing_when_not_given_flag(self):
        input_path = "test/job_no_rules_input.json"
        actual_output = main.main(input_path, option_flags=flags.Flags.NONE)

        self.assertEqual(actual_output, "[]")
