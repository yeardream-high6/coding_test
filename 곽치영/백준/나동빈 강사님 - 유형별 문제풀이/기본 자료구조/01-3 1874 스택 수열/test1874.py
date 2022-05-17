import unittest
from choconaga1874 import solve
from itertools import permutations

class Test(unittest.TestCase):
    def test_no_crash(self):
        n = 8
        for lst in permutations(range(1,n+1)):
            solve(list(lst))

if __name__ == '__main__':
    unittest.main()