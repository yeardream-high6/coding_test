from choconaga2869 import solve
import unittest

class Test(unittest.TestCase):
    def test_cases(self):
        cases = [
            {
                'input': [2, 1, 5],
                'output': 4,
            },
            {
                'input': [5, 1, 6],
                'output': 2,
            },
            {
                'input': [100, 99, 1_000_000_000],
                'output': 999_999_901,
            },
            {
                'input': [2, 1, 1],
                'output': 1,
            },
        ]
        for case in cases:
            with self.subTest(msg=f"input = {case['input']}"):
                self.assertEqual(solve(*case['input']), case['output'])

if __name__ == '__main__':
    unittest.main()