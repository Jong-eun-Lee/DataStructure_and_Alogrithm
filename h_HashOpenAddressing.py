### Hash Table 구현
## Open Addressing - Linear Probing 방법
# 작성자: 이종은

### 충돌 회피 방법(Collision Resolution Method)의 대표적 방법은 Open addressing과 Chaining.
## open addressing -> 충돌할 경우 다른 빈칸을 찾아 저장시키는 것. 한 slot당 들어갈 수 있는 entry가 하나.
# open addressing에는 linear probing, qudratic probing, double hashing 등이 있다.

# Linear Probing - 충돌이 일어나면 거기서 밑으로 고정된 이동폭에(선형적) 따라 (예를 들어 한 칸씩) 탐색하며 빈칸이면 채움.
# 마지막 슬롯이 차있으면 첫 번째로 돌아가 밑으로 다시 탐색. key 값들이 연속된 특정 슬롯에 모여 있는 것을 'cluster'라고 함.
# cluster가 많거나 그 사이즈가 크면 부정적. 탐색이나 삽입 시 충돌 이후 클러스터를 만나면 클러스터를 따라 계속 탐색해야 해서 수행 시간이 오래 걸리기 때문.
# Quadratic probing(이동폭이 제곱수.)(ex) 충돌이 일어나면 1^2칸 옮김. 거기서 또 충돌 일어나면 최초 충돌 발생한 곳에서 2^2칸 옮김. ...) 초기 해시 값이 같으면 탐사 위치가 같아 효율성 떨어짐.
# Double hashing은 2개의 hash function을 준비하여 하나는 최초 해시 값을 얻기 위해, 다른 하나는 충돌 시 이동폭을 얻기 위해 사용. 먼저 f(key)를 하고 꽉 차있으면 f(key)+g(key)로. 또 차있으면 f(key)+2*g(key)로. ...



# Hash Table 구현 by Open Addressing(Linear Probing). resize 가능.
class HashOpenAddressing: # Open Addressing 중 Linear Probnig
    def __init__(self, size = 10, ratio = 1/2):
        self.size = size # slot 개수
        self.items = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.resizeRatio = ratio
    
    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def __str__(self):
        s = "|"
        for a in self:
            if a == None:
                b = f"{'':^5}|"
            else:
                b = f"{a:^5}|"
            s += b
        return s
    
    def __len__(self):
        return self.items

    def hashFunction(self, key):
        return key % self.size

    # key 값이 있으면 해당하는 slot 번호 return. 없다면 item이 저장될 slot 번호 return.
    def findSlot(self, key): # key가 들어가게 될 slot 찾기.
        i = self.hashFunction(key)
        start = i
        while self.keys[i] != None and self.keys[i] != key:
            i = (i + 1) % self.size # 이 문장은 마지막의 다음 순서가 첫 번째로 하기 위함. 원형 구조.
            if i == start:
                return None
        return i

    def move(self): # size 늘린 새로운 table로 옮기기.
        oldSize = self.size
        oldKeys = self.keys
        oldValues = self.values
        self.size *= 2
        self.items = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size
        for i in range(oldSize):
            if oldKeys[i] != None:
                self.set(oldKeys[i], oldValues[i])
        del oldKeys
        del oldValues

    def set(self, key, value = None):
        if len(self) > self.size * self.resizeRatio: # item의 수가 슬롯 개수의 반 보다 많으면
            self.move()
            print("resize({self.size//2} -> {self.size})", end =" ")
        i = self.findSlot(key)
        if i == None:
            print("H is full now.")
            return None
        if self.keys[i] != None: # key 값이 이미 있다면
            self.values[i] = value
        else:
            self.keys[i] = key
            self.values[i] = value
            self.items += 1
        return key

    def search(self, key):
        i = self.findSlot(key)
        if i != None and self.keys[i] != None: # key가 들어갈 곳이 있고, key 값이 이미 있다면
            return self.values[i]
        else:
            return None

# H    slot 번호
# A0       0
# A1       1
# B0       2
# A3       3
# B3       4
# C0       5
#          6
# remove는 지운다고 끝나는 게 아니라. 밑에 있는 것을 지운 칸으로 옮길지 말지도 관건이다.
# 예를 들어 빈칸을 메우는 작업 없이 A1을 지우고 search(B0)를 하면 먼저 번호 0을 방문할 것인데, A0가 있어서 1로 내려가게 된다. 그런데 1이 빈칸이기 때문에 테이블에 B0이 없는 것으로 인식하게 된다(B0가 실제로 있음에도).
# 그렇다면 B0를 번호 1로 옮긴다면 번호 2가 비는데, A3를 옮겨야 할까? 아니다. 옮긴다면 search(A3)가 실패할 것이기 때문이다. 대신 번호 5에 있는 C0를 번호 2에 옮겨야 한다.
# A0       0
# B0       1
# C0       2
# A3       3
# B3       4
#          5
#          6
# C0를 옮긴 후 5번 밑인 6번으로 내려간다. 근데 6번이 빈칸이기 때문에 옮기는 작업을 종료한다.
    def remove(self, key):
        i = self.findSlot(key)
        if i == None:
            return None
        if self.keys[i] == None:
            return None
        j = i # H[i]는 지워질 슬롯, H[j]는 옮겨질 슬롯
        while True:
            self.keys[i] = None # H[i] 비우기
            while True:
                j = (j + 1) % self.size # 밑으로 내려 가기
                if self.keys[j] == None: # 밑으로 내려갔는데 빈칸이라면 작업 종료.
                    self.items -= 1
                    return key
                k = self.hashFunction(self.keys[j])
                # H[i]는 삭제하여 빈 슬롯이고, 그 아래쪽인 H[j]에 있는 아이템을 빈 슬롯 H[i]로 이동할지 말지 결정한다고 하자.
                # H[j].key 값의 hash function 값이 k라고 하면, i < k <= j일 때 H[j]를 H[i]로 옮기면 안 된다.
                # 원형 구조이기 때문에 j < i < k 나 k <= j < i 일 때도 안 된다.
                # 해당 조건인데도 옮긴다면 H[j].key 값으로 j에 있던 아이템을 찾을 때 (실제로 있음에도) 없다고 나오는 문제 등이 발생할 수 있기 때문이다.
                if not(i < k <= j or j < i < k or k <= j < i):
                    break
            self.keys[i] = self.keys[j]
            self.values[i] = self.keys[j]
            i = j
    
    # __getitem__과 __setitem__ 등의 스페셜 메소드를 이용하여
    # dict처럼 key 값으로 value를 확인하거나 item(key와 value 쌍)을 할당할 수 있다.
    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)

H = HashOpenAddressing()
H.set(0)
H.set(10)
H.set(20)
H.set(2)
H.set(7)
print(H)
H.remove(10)
print(H)
print(H.search(10))
print(H.findSlot(52))

# Linear Probing의 성능 - set, remove, search 연산 등에 대한
# 연산 시간에는 cluster size가 영향을 미치고, cluster size는 hash function, collision resolution method, load factor가 영향을 미침.
# load factor는 n/m (n은 item 개수, m은 slot 개수). load factor가 작을수록 collision 덜 발생 -> cluster size 상대적으로 크지 않게 됨. 0 <= load factor < 1
# 충돌 비율은 (collision 횟수/n).
# hash function이 c-universal로 짜여지고, m >= 2n (최소 50% 이상 슬롯이 비어있음)이라는 조건 등이 지켜질 때 평균적으로 (최악의 경우는 cluster size가 한도 끝도 없이 커지니까) 관련 연산이 O(1).
# 꼭 50퍼센트 이상이어야 그런 것은 아님. 특정 기준들 중 하나. 연산들이 평균적으로 O(1)에 수행되기 때문에 큰 데이터 등을 다루기에 적합.


### Donald Knuth의 open adressing 채택시 search 성능 관련 식
#                            linear probing           quadratic probing      
# successful search        (1/2){1 + (1/1-LF)}       1 - ln(1-LF) - LF/2           (1/LF) * ln(1/1-LF)
# unsuccessful search      (1/2){1 + 1/(1-LF)^2}     1/(1-LF) - ln(1-LF) - LF      (1/1-LF)