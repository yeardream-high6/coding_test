## sortedcontainers
리트코드는 [sortedcontainers](https://grantjenks.com/docs/sortedcontainers/) 라이브러리가 [사용 가능](https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages-)

## sortedcontainers 풀이
```python
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        slist = SortedList()
        ans = []
        for num in reversed(nums):
            ans.append(slist.bisect_left(num))
            slist.add(num)
        ans.reverse()
        return ans
```

## 바이너리 인덱스 트리
num 값이 ±10⁴로 제한되어 있으므로 펜윅 트리로 풀 수도 있습니다.  
[동빈나 - 자료구조: 바이너리 인덱스 트리(Binary Indexed Tree, BIT, 펜윅 트리) 10분 정복](https://youtu.be/fg2iGP4e2mc)