import sys

class CircularQueue:
    def __init__(self, max_size):
        self.arr_size = max_size + 1
        self.data = [None] * self.arr_size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.arr_size == self.front

    def first(self):
        if self.is_empty():
            raise Exception("CircularQueue is empty")
        return self.data[self.front]

    def append(self, item):
        if self.is_full():
            raise Exception("CircularQueue is full")
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.arr_size

    def popleft(self):
        if self.is_empty():
            raise Exception("CircularQueue is empty")
        item = self.data[self.front]
        self.front = (self.front + 1) % self.arr_size
        return item
    
    def __iter__(self):
        def generator():
            pos = self.front
            while(pos != self.rear):
                yield self.data[pos]
                pos = (pos + 1) % self.arr_size
        return generator()

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    que = CircularQueue(N)

    for i, priority in enumerate(map(int, input().split())):
        que.append((i, priority))
    
    for i in range(1, N+1):
        max_ = max(map(lambda p: p[1],que))
        while que.first()[1] != max_:
            que.append(que.popleft())
        if que.popleft()[0] == M:
            break
    
    print(i)