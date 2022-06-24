# 이중 우선순위 큐는 interval heap으로도 구현이 가능하지만
# python의 heapq를 효과적으로 사용하기 위해 두 개의 힙을 사용
# min pop해도 max heap에는 남기 때문에 삽입 삭제가 반복되면 비효율적 (분할상환을 고려해도)

import heapq as hq
import itertools

class MinHeapMaxHeap:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.min_removed = set()
        self.max_removed = set()
        self.id_counter = itertools.count()
        self.size = 0
    
    def push(self, item):
        self.size += 1
        uid = next(self.id_counter)
        hq.heappush(self.min_heap, (item, uid))
        hq.heappush(self.max_heap, (-item, uid))
    
    def _get_min(self):
        if not self.min_heap:
            return None, None
        num, uid = self.min_heap[0]
        
        while uid in self.min_removed:
            self.min_removed.remove(uid)
            hq.heappop(self.min_heap)
            if not self.min_heap:
                return None, None
            num, uid = self.min_heap[0]
        
        return num, uid
    
    def get_min(self):
        return self._get_min()[0]
    
    def pop_min(self):
        num, uid = self._get_min()
        
        if uid is not None:
            hq.heappop(self.min_heap)
            self.max_removed.add(uid)
        
        return num
    
    
    def _get_max(self):
        if not self.max_heap:
            return None, None
        num, uid = self.max_heap[0]
        
        while uid in self.max_removed:
            self.max_removed.remove(uid)
            hq.heappop(self.max_heap)
            if not self.max_heap:
                return None, None
            num, uid = self.max_heap[0]
        
        return num, uid
    
    def get_max(self):
        result = self._get_max()[0]
        return None if result is None else -result
    
    def pop_max(self):
        num, uid = self._get_max()
        
        if uid is not None:
            hq.heappop(self.max_heap)
            self.min_removed.add(uid)
            return -num
        else:
            return None
        
import sys
read_line = sys.stdin.readline

T = int(read_line())
for _ in range(T):
    heap = MinHeapMaxHeap()

    k = int(read_line())
    for _ in range(k):
        op, num_str = read_line().split()
        num = int(num_str)
        if op == 'I':
            heap.push(num)
        if op == 'D':
            if num == 1:
                heap.pop_max()
            else:
                heap.pop_min()
                
    result = [heap.get_max(), heap.get_min()]
    
    if result[0] is None:
        print("EMPTY")
    else:
        print(' '.join(map(str,result)))
