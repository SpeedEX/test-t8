import unittest

from t8.challenge2 import *


class TestChallenge2(unittest.TestCase):
    def execute(self, input_line: str, expected_result: int):
        result = solve(input_line)
        self.assertEqual(result, expected_result)

    def execute_multiple(self, test_cases):
        for case in test_cases:
            input_line, expected_result = case
            with self.subTest(input=input_line, expected=expected_result):
                self.execute(input_line, expected_result)

    def testcase1(self):
        input_line = "(A AND B AND C) OR B"
        expected_result = 0
        self.execute(input_line, expected_result)

    def testcase2(self):
        input_line = "(A AND B AND C) OR (C AND A AND C)"
        expected_result = 1
        result = solve(input_line)
        self.assertEqual(result, expected_result)

    def testcase_space(self):
        test_cases = [
            ("(A AND B AND C) OR     B", 0),
            ("(A AND B AND C) OR B    ", 0),
            ("(A AND B AND C)     OR B", 0),
            ("(A AND B AND C    ) OR B", 0),
            (" ( A  AND  B  AND C ) OR B ", 0)
        ]
        self.execute_multiple(test_cases)

    def testcase_lower(self):
        test_cases = [
            ("(a and b and c) or b", 0),
            ("(A and b and c) or b", 0),
            ("(a and b AnD c) Or b", 0)
        ]
        self.execute_multiple(test_cases)

    def testcase_parentheses(self):
        test_cases = [
            ("A", 1),
            ("(A) AND (C) AND (E)", 1),
            ("(A) AND (B) AND (E)", 0),
            ("(A)", 1),
            ("((A))", 1),
            ("((B))", 0),
            ("((A) AND (C) AND (E))", 1),
            ("((A) AND (B) AND (E))", 0),
            ("(((A)))", 1),
            ("(((B)))", 0)
        ]
        self.execute_multiple(test_cases)

    def test_complex(self):
        test_cases = [
            ("((A AND C) OR B) AND D", 0),
            ("((A AND C) OR B) OR E", 1),
            ("(A AND B) AND (C AND D) AND (A)", 0),
            ("(A OR B) AND (C OR D) AND (A)", 1),
            ("D AND (B OR (A AND C))", 0)
        ]
        self.execute_multiple(test_cases)

    def test_debug(self):
        self.execute("(A)", 1)


if __name__ == '__main__':
    unittest.main()
