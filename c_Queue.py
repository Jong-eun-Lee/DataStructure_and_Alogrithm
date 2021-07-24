## Queue
# 작성자: 이종은

# FIFO 규칙의 순차적 자료구조
# 삽입 연산: enqueue
# 삭제 연산: dequeue

class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0
    
    def enqueue(self, val):
        self.items.append(val)
    
    def dequeue(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("Queue is empty")
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x
    # items에서 지우진 않고 index만 조정
    # pop(0)말고 이렇게 구현하는 이유?
    # dequeue 연산을 상수 시간에 수행되도록 하기 위해
    ## 실제로 지우면서, dequeue 연산을 상수 시간에
    ## 수행되게 하는 원형, 동적 배열식
    ## ArrayQueue 클래스를 본 파일 말미에 만듦

    def front(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("Queue is empty")
        else:
            return self.items[self.front_index]
    
    def __len__(self):
        return len(self.items) - self.front_index

    def isEmpty(self):
        return len(self) == 0



## Stack + Queue = Deque
# 양쪽에서 삽입과 삭제가 가능

from collections import deque
D = deque()
D.append(10)
D.appendleft(1)
D.append(20)
D.appendleft(2)
print(D)
D.pop()
D.popleft()
print(D)



## Array_Queue
# dequeue 시 실제로 삭제
# dequeue 연산 O(1) in amortized analysis
# 원형 배열 by 인덱스 계산 부분 수정
# 동적 배열

class ArrayQueue:
    default_capacity = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.default_capacity
        self.size = 0
        self.front = 0

    def resize(self, capa):
        cur = self.data
        self.data = [None] * capa
        walk = self.front
        for k in range(self.size):
            self.data[k] = cur[walk]
            walk = (walk + 1) % len(cur)
        self.front = 0

    def enqueue(self, val):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = val
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
        result = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return result

    def first(self):
        if self.isEmpty():
            print('Queue is empty')
        return self.data[self.front]
        
    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0