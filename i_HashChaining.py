## Hash Table (Chaining 방법) 구현
# 작성자: 이종은

# oepn addressing과 대비되는 다른 충돌 회피 방법은 chaining.
# open addressing은 한 slot당 들어갈 수 있는 entry가 하나지만 chaining은 아님.
# chaining은 하나의 slot에 여러 개의 item 들어갈 수 있다. 각 slot은 연결리스트로 관리하겠음.
# 3번에 23 넣을 때 pushFront(23)가 O(1)이니 set(23)도 O(1)
# search(66)와 remove는 O(충돌 key의 평균 개수(=연결리스트 길이))
# 해쉬 펑션을 c-universal로 잘 짜면 슬롯당 연결리스트의 평균 길이는 O(1) 이다. search, remove 평균적으로 O(1)에 가능하게.
# 3번 슬롯 -> 13 -> None
# 3번 슬롯 -> 23 -> 13 -> None

# Pr(f(x)==f(y)) = c/m 일 때 c-universal

# open adressing과 마찬가지로 c-universal 해시함수로 짜고, 빈 slot을 충분히 유지한다고 하면 평균적으로 O(1)
# Open Addressing의 Linear Probing 방법과 Chaining 방법의 탐색 시간을 비교할 경우 LF가 약 0.85 전에는 Linear Probing의 탐색이 더 빠르지만 그 이후에는 Linear Probing의 탐색 시간이 Chaining에 비해 급격히 느려진다.

# 각 slot은 한방향 연결리스트로 관리하겠음.
class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.key)

class SinglyLinkedListForHash:
    def __init__(self):
        self.head = None

    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
    
    def __str__(self):
        return " -> ".join(str(v.key) for v in self) + " -> None"
    
    def pushFront(self, key, value=None):
        v = Node(key)
        v.next = self.head
        self.head = v
    
    def popFront(self):
        if self.head == None:
            return None
        else:
            key = self.head.key
            self.head = self.head.next
            return key

    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return v

    def remove(self, v):
        if v == None or self.head == None:
            return None
        key = v.key
        if v == self.head:
            return self.popFront()
        else:
            prev = None
            cur = self.head
            while cur != None and cur != v:
                prev = cur
                cur = cur.next
            if cur == v:
                prev.next = cur.next
            return key

class HashChaining:
    def __init__(self, size=10):
        self.size = size
        self.H = [SinglyLinkedListForHash() for x in range(self.size)]
    
    def __iter__(self):
        for i in range(self.size):
            yield self.H[i]
    
    def __str__(self):
        s = ""
        i = 0
        for sl in self:
            s += f"|{i:^3}|" + str(sl) + "\n"
            i += 1
        return s
        
    def hashFunction(self, key):
        return key % self.size
    
    def findSlot(self, key):
        return self.hashFunction(key)

    def set(self, key, value=None):
        i = self.findSlot(key)
        v = self.H[i].search(key)
        if v == None:
            self.H[i].pushFront(key, value)
        else:
            v.value = value

    def search(self, key):
        i = self.findSlot(key)
        v = self.H[i].search(key)
        if v == None or v != key:
            return None
        else:
            return key
        
    def remove(self, key):
        i = self.findSlot(key)
        v = self.H[i].search(key)
        if v == None:
            return None
        elif v == self.H[i].head:
            self.H[i].popFront()
        else:
            prev = self.H[i].head
            while prev.next != v:
                prev = prev.next
            prev.next = v.next
        return key

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)

H = HashChaining()
H.set(1)
H.set(23)
H.set(3)
H.set(13)
print(H)
H.remove(23)
H.remove(13)
print(H)
print(H.H[1].search(1))