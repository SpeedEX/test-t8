import unittest

from t8.challenge3 import *


class TestChallenge3(unittest.TestCase):
    def execute(self, input_line: str, expected_result: str):
        result = solve(input_line)
        self.assertEqual(result, expected_result)

    def execute_multiple(self, test_cases):
        for case in test_cases:
            input_line, expected_result = case
            with self.subTest(input=input_line, expected=expected_result):
                self.execute(input_line, expected_result)

    def test_example1(self):
        input_line = "[['Apple', 'Banana', 'Cherry'], 'Tomato']"
        expected_result = """["Cherry, Tomato"]"""
        self.execute(input_line, expected_result)

    def testcase1(self):
        input_line = "[[Dog, Cat, 'Horse'], 'Hippo']"
        expected_result = """["Horse, Hippo"]"""
        self.execute(input_line, expected_result)

    def testcase2(self):
        input_line = "[['Plane', 'Plane', 'Plane', 'Jet'], 'Air']"
        expected_result = """["Plane, Jet, Air"]"""
        result = solve(input_line)
        self.assertEqual(result, expected_result)

    def testcase_space(self):
        test_cases = [
            ("  [['Apple', 'Banana', 'Cherry'], 'Tomato']  ", """["Cherry, Tomato"]"""),
            ("  [['Apple'  ,   'Banana'  , 'Cherry']  , 'Tomato']  ", """["Cherry, Tomato"]"""),
            ("[['Apple','Banana','Cherry'],'Tomato']", """["Cherry, Tomato"]""")
        ]
        self.execute_multiple(test_cases)

    def testcase_small_queue(self):
        test_cases = [
            ("""[[], '']""", """[""]"""),
            ("""[[], 'new item']""", """["new item"]"""),
            ("""[['1 item'], '']""", """[""]"""),
            ("""[['item 2', 'item 2'], 'new item']""", """["new item"]"""),
        ]
        self.execute_multiple(test_cases)


if __name__ == '__main__':
    unittest.main()
