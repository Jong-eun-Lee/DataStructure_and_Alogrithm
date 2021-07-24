## 원형 양방향 연결리스트로 '덱' 구현(CircularDoublyLinkedDeque)
# 작성자: 이종은

# 앞서 만든 원형 양방향 연결리스트와는 조금 다르게
# (splice 연산 없는 등)
# 이번엔 key 대신 element로 표기.
class CircularDoublyLinkedBase:
    class Node:
        __slots__ = "element", "prev", "next" # __slots__ 해주는 건 메모리 절약용

        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next
        
        def __str__(self):
            return str(self.element)

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0
    
    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insertBetween(self, e, pred, succ):
        new = self.Node(e, pred, succ)
        pred.next = new
        succ.prev = new
        self.size += 1
        return new

    def deleteNode(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element
    
    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            assert isinstance(v.next, object) # assert 뒤의 조건이 True가 아니면 에러 발생
            v = v.next
    
    def __str__(self):
        return " <-> ".join(str(v) for v in self)
    
class Empty(Exception): # 파이썬 내장 클래스 Exception을 상속해서 예외 만들어 주기
    pass

class CircularDoublyLinkedDeque(CircularDoublyLinkedBase):
    def first(self):
        if self.isEmpty():
            raise Empty("Deque is empty") # raise는 일부러 에러 발생시키는 것
        return self.head.next.element
    
    def last(self):
        if self.isEmpty():
            raise Empty("Deque is empty")
        return self.head.prev.element

    def insertFirst(self, e):
        self.insertBetween(e, self.head, self.head.next)
    
    def insertLast(self, e):
        tail = self.head
        self.insertBetween(e, tail.prev, tail)
    
    def deleteFirst(self):
        if self.isEmpty():
            raise Empty("Deque is empty")
        return self.deleteNode(self.head.next)
    
    def deleteLast(self):
        if self.isEmpty():
            raise Empty("Deque is empty")
        tail = self.head
        return self.deleteNode(tail.prev)

D = CircularDoublyLinkedDeque()
D.insertFirst(3)
D.insertFirst(1)
D.insertLast(5)
D.deleteLast()
print(D)