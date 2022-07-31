# 세그먼트 트리 설명 - 안경잡이개발자 https://m.blog.naver.com/ndb796/221282210534
# 세그먼트 트리 효율적인 구현 https://gyutaelee.github.io/algorithm/Efficient-and-easy-segment-trees/

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        # 2n 길이의 이진 트리를 만듭니다.
        # 1이 루트노드이며, 0은 사용하지 않습니다 (계산 편의상)
        # 마지막 n개 노드가 리프노드가 됩니다.
        
        # 트리 인덱스 빠른 계산 방법
        # parent = curr >> 1
        # lchild = curr << 1
        # rchild = lchild | 1
        # sibling = curr ^ 1
        
        tree = nums * 2
        
        # n ~ 1 까지 역순으로 돌면서 두 자식의 합으로 초기화합니다.
        for i in range(n-1, 0, -1):
            lchild = i << 1
            tree[i] = tree[lchild] + tree[lchild | 1]
        
        self.tree = tree
        self.n = n

    def update(self, index: int, val: int) -> None:
        tree = self.tree
        
        # 리프노드 값을 수정합니다.
        child = self.n + index
        tree[child] = val

        # 부모 노드부터 시작합니다.
        curr = child >> 1
        while curr:
            # 부모 노드의 값을 두 자식으로부터 업데이트합니다.
            tree[curr] = tree[child] + tree[child ^ 1]

            child = curr
            curr = child >> 1
        

    def sumRange(self, left: int, right: int) -> int:
        n = self.n
        tree = self.tree
        
        # left, right에 해당하는 리프노드를 찾습니다.
        # 이때 [left, right) 범위, 즉, left는 포함하고, right는 포함하지 않는 인덱스를 사용합니다. (계산 편의상)
        left += n
        right += n + 1
        
        result = 0
        
        while left < right:
            # left가 오른쪽 자식이면, 해당 범위를 합산하고 떼어냅니다.
            if left & 1:
                result += tree[left]
                left += 1
            left >>= 1
            
            # right-1가 왼쪽 자식이면, 해당 범위를 합산하고 떼어냅니다.
            if right & 1:
                result += tree[right - 1]
            right >>= 1
        
        return result