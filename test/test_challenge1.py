import unittest

from t8.challenge1 import *


class TestChallenge1(unittest.TestCase):
    def execute(self, input_line: str, expected_result: str):
        result = solve(input_line)
        self.assertEqual(result, expected_result)

    def execute_multiple(self, test_cases):
        for case in test_cases:
            input_line, expected_result = case
            with self.subTest(input=input_line, expected=expected_result):
                self.execute(input_line, expected_result)

    def testcase1(self):
        input_line = "[8, 2, 8, 1, 9]"
        expected_result = "10 (2 + 8)"
        self.execute(input_line, expected_result)

    def testcase2(self):
        input_line = "[8, 8, 8, 8, 8]"
        expected_result = "16 (8 + 8)"
        self.execute(input_line, expected_result)

    def testcase_small_list(self):
        test_cases = [
            ("", "input contains less than 2 numbers"),
            ("[]", "input contains less than 2 numbers"),
            ("[1]", "input contains less than 2 numbers"),
            ("[10, 9]", "19 (10 + 9)"),
            ("[1, 3, 2]", "4 (2 + 2)"),
        ]
        self.execute_multiple(test_cases)

    def test_space(self):
        test_cases = [
            (" [ 8 ,  2 ,  8 ,  1 ,  9 ] ", "10 (2 + 8)"),
            ("[8,2,8,1,9]", "10 (2 + 8)")
        ]
        self.execute_multiple(test_cases)


if __name__ == '__main__':
    unittest.main()
