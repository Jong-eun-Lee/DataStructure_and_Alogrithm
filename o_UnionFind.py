## Union-find 자료구조(disjoint set 자료구조)
# 작성자: 이종은

# 집합에 대한 연산을 효율적으로 제공하기 위한 자료구조
# 1. membership 연산 ex) a ∈ S -> T/F?
# 2. union, intersection, difference

# makeSet(x): x만으로 구성된 집합을 만드는 것.
# find(x): membership function임. x가 속한 집합의 대표값을 return.
# union(x, y): x와 y는 key 값. 두 개가 서로 다른 집합에 속한다면 하나의 집합으로 union.
# make-set은 O(1). find와 union은 1차적으로 O(log n)이지만, 더 줄일 수 있는지 확인.

# 첫 번째 구현 방법: by 원형 양방향 연결리스트
# makeSet(x): 더미 노드와 x가 서로 링크
# v = find(x) x가 속한 원형 양방향 연결리스트의 더미 노드를 return
# union(x, y): v = find(x), w = find(y) 실행 후
# if v != w: join(v, w) -> v가 속한 연결리스트와 w가 속한 연결리스트를 연결
# find와 union 연산은 최악의 경우 O(n)임.

# 두 번째 구현 방법: by 트리
# 각 노드는 부모를 가리키는 링크만 갖고 있음.
# 루트 노드는 자기 자신을 가리킴.
# find(x)에서 parents 따라 올라가 return하는 건 루트 노드. 루트 노드가 집합 대표.
# union(x, y): v=find(x), w=find(y) 후 
# if v != w: 일정한 규칙에 따라 v가 w를 부모로 가리키거나 w가 v를 부모로 가리킴.
# v와 w의 높이를 비교해서 높이가 더 작은 집합의 루트 노드가 높이가 더 큰 집합의 루트 노드를 가리키도록 함.
# if v.height > w.height: w.parent = v
# elif v.height < w.height: v.parent = w
# else면 어느 쪽이든 상관 없이 연결.
# find(x), union(x, y): O(h)
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0 # height를 union-find에선 rank라고 하겠음.
    
    def makeSet(x):
        return Node(x)

    def find(x):
        while x.parent != x:
            x = x.parent
        return x
    
    def union(x, y):
        v = self.find(x)
        w = self.find(y)
        if v.rank > w.rank: # rank가 다르면 v와 w는 다른 것.
            v, w = w, v # w의 rank가 더 크거나 같은 걸로 지정.
        v.parent = w
        if v.rank == w.rank:
            w.rank += 1

# Nh를 높이가 h인 트리의 최소 노드 개수라고 하면
# N0 = 1 ; N1 = 2 ; N2 = 4 ; Nh = 2 * N(h-1) = 2^h * N0
# Nh = 2^h
# n >= 2^h
# log n >= h
    
# log n보다 더 좋게 하려면
# find 연산을 조정해야 한다.