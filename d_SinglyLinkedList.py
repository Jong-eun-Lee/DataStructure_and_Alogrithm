## SinglyLinkedList(한방향 연결리스트)
# 작성자: 이종은

# 배열과 파이썬의 리스트는 접근이 상수 시간에 가능
# 삽입과 삭제 연산은 최악의 경우 O(n)
# 반면
# 연결리스트(한방향 or 양방향)는
# 접근이 최악의 경우 O(n)(꼬리에 꼬리를 물고 링크를 따라가야 해서),
# 삽입과 삭제 연산은 O(1)에 수행됨
# 노드는 key 값과 link(다음 노드를 가리키는 정보)로 이루어짐
# key와 link 말고 별도의 value 값을 가지고 있을 수도 있음
# key와 link는 필수지만, value는 필수가 아님.
# 맨 첫 번째 노드는 head node
# 마지막 노드(tail node)는 None을 가리킴

class Node:
    def __init__(self, key=None, value=None):
        self.key = key # key라는 멤버에 parameter로 주어진 key를 전달해 줌.
        self.value = value # value는 필수는 아니지만, 멤버로 해줌
        self.next = None # link를 next라 하겠음.

    def __str__(self):
        return str(self.key)
        # key가 3인 노드 v의 key 값을 출력하려면
        # print(v.key)를 해야 하는데,
        # 클래스에 __str__ 스페셜 메소드를 이렇게 만들어주면,
        # print(v)만 해도 3이 (문자열로) 출력됨.
        # 내부적으로 보면 print(v)를 해주면 Node라는 클래스에 __str__가 정의돼 있는지 확인하고,
        # 있다면 print(v.__str__())이 실행됨.



class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    # 해당 클래스는 일단
    # head node 가리키는 정보와 노드 개수인 size 정보만
    # 여러 노드 생성해서 잇는 게 아니라

    def __str__(self):
        s = ""
        v = self.head
        while v:
            s += str(v.key) + " -> "
            v = v.next
        s += "None"
        return s

    def __len__(self):
        return self.size

    # 삽입 연산
    # pushFront는 head node 앞에 새로운 노드 삽입.
    # pushBack은 tail node 다음에 새로운 노드 삽입.
    
    def pushFront(self, key=None, value=None):
        v = Node(key, value)
        v.next = self.head
        self.head = v
        self.size += 1
    # O(1)

    def pushBack(self, key=None, value=None):
        v = Node(key, value)
        if len(self) == 0:
            self.head = v
            # 아무 것도 없는 리스트에 들어갈 경우
            # 그것이 head node이자 tail node
        else:
        # tail에 대한 정보를 안 갖고 있으니
        # tail을 찾아 head부터 찾아 내려감.
            tail = self.head
            while tail.next != None:
                tail = tail.next
            # 다음이 None인 node가 tail node
            tail.next = v
        self.size += 1 # 노드 개수 하나 늘어남.
    # O(n)

    # 삭제 연산
    # popFront: head node 삭제
    # popBack: tail node 삭제

    def popFront(self):
        key = value = None
        if len(self) > 0:
            key = self.head.key
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
        return key, value
    # O(1)
    
    def popBack(self):
        if len(self) == 0: return None, None
        else:
            prev, cur = None, self.head
            while cur.next != None:
                prev = cur
                cur = cur.next
            tail = cur
            key, value = tail.key, tail.value    
            if self.head == tail:
                self.head = None
            else:
                prev.next = tail.next
                self.size -= 1
            return key, value
    # O(n)

    # 탐색(search)
    # generator 정의 후 만드는 게 더 간단
    #def search(self, key):
    ### key 값의 노드를 리턴, 없으면 None 리턴
    #    v = self.head
    #    while v:
    #        if v.key == key:
    #            return v
    #        v = v.next
    #    return None # return v이라 써도 None이 나올 것
    # O(n)

    # 제네레이터(generator)
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
        # yield를 활용해야 generator
        # __iter__라는 스페셜 메소드가 정상적으로 구현돼 있어야
        # for a in L:
        #   print(a)
        # 와 같은 문장을 쓸 수 있음.
        # 이런 for 문이 실행 되면
        # L이라는 객체의 __iter__ 있는지 메소드 호출
        # yield v를 통해 a가 v로 됨.
        # 그 다음 print(a) 실행
        # 그 다음 for loop 다시 접근
        # 그 다음 yield v 밑에 있는 v = v.next 실행
        # while 문 실행. v가 None이 아니면 다시 yield 실행.
        # 이 yield에 의해 전달받은 게 a가 됨.
        # ...
        # while 문이 끝나면 StopIteration Error 메시지 생성
        # 생성된 메시지 관측되면 for 문에서 나옴

    # generator 만들고 난 후에 search 함수 정의하면
    # 위에서 만든 search 함수보다
    # 더 간단하게 작성 가능
    def search(self, key):
        for v in self:
            if v.key == key:
                return v
        return None

    def remove(self, key):
        v = self.search(key)
        if len(self) == 0:
            return False # 제거 실패하면 False
        
        if v == self.head:
            self.popFront()
        else:
            prev = self.head
            while prev.next != v:
                prev = prev.next
            prev.next = v.next
            self.size -=1
        return True # 제거 성공하면 True
        # 최악의 경우 O(n). 양방향 연결리스트에선 이 단점을 보완 가능.

    def isEmpty(self):
        return len(self) == 0



S = SinglyLinkedList()
S.pushBack(2)
print(S)
S.pushFront(1)
S.pushBack(100)
S.remove(100)
S.pushBack(4)
print(S)
for x in S:
    print(x)
print(S.__dict__)