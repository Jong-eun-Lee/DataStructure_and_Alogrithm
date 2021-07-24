## CircularDoublyLinkedList(원형 양방향 연결리스트)
# 작성자: 이종은

# Node class에 next link말고도
# prev를 추가하자. 그리고
# tail node의 next를 head를 가리키도록 하자.
# '원형' 양방향 연결리스트로.
# 최초 생성되는 빈 리스트는 head node의
# key가 None이고, prev와 next가 자기 자신을 가리킴.
# 여기서 head node는 dummy node. 이것의 key 값은 의미 없음. 항상 None으로.
# splice 연산을 구현하여 이동, 삽입 연산 등을 만든다!
class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.key)

class CircularDoublyLinkedList:
    def __init__(self): # 해당 리스트는 head와 size를 가리키는 정보 가짐.
        self.head = Node() # key가 None인 dummy node 생성.
        self.size = 0 # head node는 size에 count 안 됨.
    
    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
        return " <-> ".join(str(v) for v in self)

    def __len__(self):
        return self.size

    # splice 연산
    # a부터 b까지를 떼다가 x 다음에 넣음.
    # 조건 1: a 다음에 b가 나와야
    # 조건 2: a와 b 사이에 head가 없어야.
    # 조건 3: a와 b 사이에 x가 없어야.
    # 6개의 링크를 바꿔야 함.
    def splice(self, a, b, x): # a, b, x는 각각 노드
        a.prev.next = b.next
        b.next.prev = a.prev
        # a부터 b까지 cut 됨.
        b.next = x.next
        x.next.prev = b
        x.next = a
        a.prev = x
        # a부터 b까지 x 다음에.
    # O(1). 6개 링크만 수정해주니까.
    
    # 이동 연산
    def moveAfter(self, a, x):
        # 노드 a를 노드 x 다음으로.
        self.splice(a, a, x)
    # O(1)
    
    def moveBefore(self, a, x): # 노드 a를 x 전에
        self.splice(a, a, x.prev)
    # O(1)

    # 삽입 연산
    def insertAfter(self, key, x):
        # key 값을 가진 새로운 노드를 만든 후 x node 다음에 집어 넣기
        self.moveAfter(Node(key), x)
        self.size += 1
        # prev와 next가 자기 자신을 가리키는, key 값을 가진 Node가 생성되는데,
        # 이게 x 다음으로 옮겨짐.
    # O(1)
    
    def insertBefore(self, key, x):
        self.moveBefore(Node(key), x)
        self.size += 1
    # O(1)
    
    def pushFront(self, key): # 새로운 노드를 head 다음에
        self.insertAfter(key, self.head)
        self.size += 1
    # O(1)

    def pushBack(self, key): # 새로운 노드를 head 전에
        self.insertBefore(key, self.head)
        self.size += 1
    # O(1)

    # 탐색 연산
    def search(self, key):
        v = self.head.next
        while v != self.head:
            if v.key == key:
                return v
            v = v.next
        return None
    # O(n)

    # 삭제 연산

    # key 값을 지우는 게 아니라
    # search를 통해 특정 key 값을 가진
    # node를 찾아내서 node를 삭제해야 함.
    def remove(self, x): # 노드 x를 삭제
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
        del x
    # O(1)
    # remove 자체는 상수 시간에 수행되는데,
    # 지울 노드를 그냥 전달해 주니까.
    # 근데 그 전에 지울 노드를 search를 통해 알아야 하는 점을 유의해야 함.

    def popFront(self):
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        self.remove(self.head.next)
        self.size -= 1
        return key
    # O(1)

    def popBack(self):
        if self.head.prev == self.head:
            return None
        key = self.head.prev.key
        self.remove(self.head.prev)
        self.size -= 1
        return key
    # O(1)
    
    def join(self, L): # 현재 리스트 뒤에 다른 리스트 이어 붙이기
        self.splice(L.head.next, L.head.prev, self.head.prev)
        self.size += len(L)

    def split(self, x): # 노드 x부터 tail node까지 떼어 새로운 리스트 만들어 return.
        L = CircularDoublyLinkedList()
        self.splice(x, self.head.prev, L.head)
        return L

    def isEmpty(self):
        return len(self) == 0
    
    def first(self):
        if self.isEmpty():
            return None
        return self.head.next
    
    def last(self):
        if self.isEmpty():
            return None
        return self.head.prev

C = CircularDoublyLinkedList()
C.insertAfter(3, C.head)
C.insertAfter(4, C.search(3))
C.insertAfter(5, C.search(4))
C.pushBack(777)
C.remove(C.search(777))
C.splice(C.search(3), C.search(4), C.search(5))
print(C)
for v in C:
    print(v)