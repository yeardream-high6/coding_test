from collections import Counter

def solution(numbers):
    if all(num == 0 for num in numbers):
        return "0"
    
    # 길이 적어도 6이 되도록 반복한 값으로 정렬합니다.
    def repeat(num_str):
        l = len(num_str)
        repeat = {
            1: 6,
            2: 3,
            3: 2,
            4: 2,
        }
        return num_str * repeat[l]
    counter = Counter((repeat(num_str), num_str) for num_str in map(str,numbers))
    answer = [num_str * count for (_, num_str), count in sorted(counter.items(), reverse=True)]
    return ''.join(answer)

import unittest

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([6, 10, 2]), "6210")
        self.assertEqual(solution([3, 30, 34, 5, 9]), "9534330")
    def test2(self):
        self.assertEqual(solution([5, 54, 552]), "555254")
    def test3(self):
        self.assertEqual(solution([576, 575, 57, 574, 536, 535, 53, 534, 5]), "576"+"57"+"575"+"574"+"5"+"536"+"535"+"53"+"534")
    def test4(self):
        self.assertEqual(solution([1000, 101, 100, 10, 1, 0]), "1"+"101"+"10"+"100"+"1000"+"0")
    def test5(self):
        self.assertEqual(solution([0, 0, 0, 0]), "0") # ?!?!?! 이건 함정이다!

if __name__ == '__main__':
    unittest.main()