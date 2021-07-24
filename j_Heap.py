## Heap(힙) (max heap - 부모 노드의 key가 자식 노드의 key보다 크거나 같음)
# 작성자: 이종은

# 트리 표현법(리스트 등을 트리로 해석)
#     a
#    / \ 
#   b   c
#  / \ / \
#    d e

# 표현법 1: 리스트: level 0 -> level 1 -> ... # A = [a, b, c, None, d, e]
# level 0은 A[0], level 1은 A[1]과 A[2], ...
# A[k]의 왼쪽 자식 노드 인덱스는 A[2*k+1]. # A[k]의 부모 노드 인덱스는 A[(k-1)//2]. # 상수 시간에 자식 노드와 부모 노드를 알 수 있음. O(1). # 중간에 없는 노드를 모두 None으로 표시하여 메모리 낭비가 있을 수 있음(Heap의 경우 중간에 None이 없음).

# 표현법 2: 리스트(재귀적): # A = [a, [a의 왼쪽 부트리(subtree)], [a의 오른쪽 부트리]] # = [a, [b, [], [d, [], []]], [c, [e, [], []]]]

# 표현법 3: 노드 class(직접 정의) # key 값, 자식 노드 가리키는 링크 두 개(left와 right), 부모 노드 가리키는 링크(parent) 등 최소 4개 갖는 노드 class 정의

## Heap을 첫 번째 표현법을 이용하여 구현해본다.
# Heap의 조건은 다음과 같다.
#           51
#         /    \
#        33    16
#       / \    / \
#      25  7  5   2
#     /
#    1
# 1. 모양 조건: 완전 이진 트리 형태여야 한다(마지막 레벨의 경우 노드가 꽉 차지 않아도 되지만, 왼쪽부터 차례대로 채워져야 함).
# 2. 값 조건: 모든 부모 노드의 key 값은 자식 노드의 key 값보다 작지 않다.
# heap의 루트 노드는 가장 큰 값을 가짐.(=A[0] 가장 큼)(max heap의 경우임).

class Heap:
    def __init__(self, L=[]):
        self.A = L
    
    def __str__(self):
        return str(self.A)
    
    def __len__(self):
        return len(self.A)

    def makeHeap(self): # 힙의 값 조건 만족하도록 리스트 재배열
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.heapifyDown(k, n) # k는 A[k]의 인덱스. n은 전체 노드 개수
        # O(n) <- O(n * log n) = O(n * h) (h는 heap의 높이)
        # 대략적으로 계산하면 O(n * log n)이지만,
        # tight하게 볼 때 O(n)으로 계산할 수 있는 증명은 밑에서 서술하겠다.

    def heapifyDown(self, k, n): # heap 성질을 만족하도록 하는 연산
        while 2*k + 1 < n:  # A[k]가 리프 노드가 아니면
            left, right = 2*k + 1, 2*k + 2
            if left < n and self.A[left] > self.A[k]:
                max = left
            else:
                max = k
        
            if right < n and self.A[right] > self.A[max]:
                max = right
        
            if max != k:
                self.A[k], self.A[max] = self.A[max], self.A[k]
                k = max
            else:
                break
    # 최악의 경우 O(h) = O(log n)

### O(h)는?
# 높이가 h인 힙의 전체 노드 수를 n개라고 하자. 마지막 레벨은 레벨 h.
# h-1 레벨의 노드 개수는 2^(h-1).
# 마지막 레벨은 최소 한 개이므로
# 1 + 2 + 2^2 + ... + 2^(h-1) + 1 <= n 
# (2^h - 1)/(2 - 1) + 1 = 2^h <= n
# h <= log2 n 
# ∴ O(h) = O(log n)

### makeHeap은 어떻게 O(n)까지 가능?
# 모든 레벨이 노드가 꽉찬 정이진트리 형태의 힙이 있다고 하자.
# 높이가 h라 하면 전체 노드 수는 2^(h+1)-1. 전체 노드 수를 n이라 하자.
# 레벨 h의 노드 개수는 2^h = {2^(h+1)-1 + 1}/2 = (n+1)/2
# 레벨 h-1의 노드 개수는 2^(h-1) = {2^(h+1)-1 + 1}/2^2 = (n+1)/2^2
# ...
# heapifyDown 연산 시간은 힙의 높이에 비례한다. 이 점을 반영하여 makeHeap의 시간복잡도를 고려해보면
# 0*(n+1)/2 + 1*(n+1)/2^2 + 2*(n+1)/2^3 + 3*(n+1)/2^4 + ...
# = 0 + (n+1)/2^2*(1 + 2/2 + 3/2^2 + ...)
# = (n+1)/4*c = O(n)
# ∴ O(n)

    # 가장 큰 걸 맨 오른쪽으로 보내고
    # 루트노드부터 히피파이 다운하면
    # 두 번째로 큰 게 맨 오른쪽에서 두 번째로 가고
    # 해서 오름차순으로 
    def heapSort(self):
        # 루트 노드와 마지막 노드를 바꾸고 루트에서 heapifyDown.
        # heapifyDown 후 두 번째로 큰 값이 루트 노드에 올라오게 되는데, 이것을 끝에서 두 번째 노드와 바꿔 루트에서 heapifyDown.
        # ...
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n -= 1 # 바꾼 큰 값을 제외하고 heapifyDown하도록 n을 줄임.
            self.heapifyDown(0, n)
    # O(n*log n)
    
    def insert(self, key):
        self.A.append(key)
        self.heapifyUp(len(self.A) - 1)
    # O(log n)
    # insert n번 해서 힙 만들면 O(n*log n)인데,
    # makeHeap으로 O(n)만에 하는 것이 낫다.

    def heapifyUp(self, k):
        while k > 0 and self.A[(k-1)//2] < self.A[k]:
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            k = (k-1)//2
        # 최악의 경우 루트 노드까지 도달.
    # O(log n)

    def findMax(self):
        return self.A[0]
    # O(1)

    def deleteMax(self):
        # 루트 노드 제거 후 마지막 노드를 루트 노드에 올리고,
        # 힙 성질 만족하도록 내려 보냄.
        if len(self.A) == 0:
            return None
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        self.A.pop()
        self.heapifyDown(0, len(self.A)) # pop해서 기존 길이보다 1만큼 적어졌을 것.
        return key
    # O(log n)



S = [100, 5, 3, 7, 9, 14, 11, 23, 4]
H = Heap(S)
H.makeHeap()
H.insert(1)
H.deleteMax()
print(H, end="\n\n")
H.heapSort()
print(H)