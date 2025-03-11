import unittest


from ci_test import main


class MainIntegrationTest(unittest.TestCase):
    def test_main_returns_expected_output(self):
        input_path = "test/input.json"
        actual_output = main.main(input_path)

        expected_output_path = "test/output.json"

        with open(expected_output_path) as f:
            expected_output = f.read()

        self.assertEqual(actual_output, expected_output)
