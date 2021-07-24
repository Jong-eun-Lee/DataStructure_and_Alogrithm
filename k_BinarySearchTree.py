## Binary Search Tree(BST)(이진 탐색 트리)
# 작성자: 이종은

# 이진 탐색 트리의 성질: 특정 노드 v의 key 값은 왼쪽 자손 노드들(왼쪽 부트리)보다 크고, 오른쪽 자손 노드들보다 작다.
# 이를 통해 search를 더 효율적으로 할 수 있게 한다. 모든 노드를 샅샅이 뒤지는 게 아니라 루트 노드부터 비교해서 찾으려는 key 값이 더 크면 오른쪽으로 내려가고, 거기서 또 비교해서 왼쪽이나 오른쪽으로 내려가며 이 과정을 계속한다.
# search는 O(h)로 이진 탐색 트리의 높이를 최대한 작게 할수록 탐색이 효율적이게 될 것이다.

class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.key)
    
# traversal(순회) 1. preorder traversal 2. inorder traversal 3. postorder traversal
# 자기 자신을 M, 왼쪽 부트리를 L, 오른쪽 부트리를 R이라고 하면 # 1. preorder: MLR(M이 앞에) # 2. inorder: LMR(M이 가운데에) # 3. postorder: LRM(M이 마지막에)
# L을 R보다 먼저 방문하는 게 공통점. 부트리에 들어갈 때는 재귀적으로 다시 order를 따름.
#     A
#    / \
#   B   C
#  /\    \
# D  E    F
#   /\    /
#  G  H  I
# postorder(전위): A B D E G H C F I
# inorder(중위): D B G E H A C I F
# postorder(후위): D G H E B I F C A

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)
    
    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def findLocation(self, key):
    # key 값에 해당하는 노드가 있다면 그것을 return.
    # tree에 없다면 key 값을 가진 노드가 삽입될 자리의 '부모 노드'를 return.
        if self.size == 0:
            return None # 루트 자리에 들어가야 하는데, 루트 노드 부모가 None이므로.
        v= self.root
        p = None # p는 v의 parent
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p
    # O(h)

    def search(self, key):
        v = self.findLocation(key)
        if v and v.key==key:
            return v
        else:
            return None
    # O(h)

    def insert(self, key):
        p = self.findLocation(key)
        if p != None and p.key == key:
            print("The key is already in tree")
            return
        else:
            v = Node(key)
            if p == None:
                self.root = v
            else: # p.key != key
                v.parent = p
                if p.key > key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
    # O(h)

    def deleteByMerging(self, x):
        # 삭제할 노드를 x, x의 왼쪽 부트리를 L, 오른쪽 부트리를 R이라고 하면
        # x 삭제 후, 그 자리에 L이 오도록 한 뒤 L에서 가장 값이 큰 노드의 오른쪽 자식에 R을 붙임.
        l, r, p = x.left, x.right, x.parent
        if l == None: # L이 없다면 x 자리에 오는 replace는 R이 와야 함.
            replace = r
        else:
            replace = m = l # replace와 m은 l. m은 L에서 가장 값이 큰 노드
            while m.right:
                m = m.right
            m.right = r # m의 오른쪽 자식으로 R을 붙임
            if r:
                r.parent = m
        
        if self.root == x:
            if replace:
                replace.parent = None
            self.root = replace
        else:
            if p.left == x:
                p.left = replace
            else:
                p.right = replace
            if replace:
                replace.parent = p
        self.size -= 1
    # O(h)
    
    def deleteByCopying(self, x):
        # L에서 가장 값이 큰 노드를 x 자리에.
        l, r, p = x.left, x.right, x.parent
        if l == None:
            replace = r
        else:
            m = l
            while m.right:
                m = m.right
            m.parent.right = m.left # if m.left: 전에 미리 해야 유효함을 주의. 그렇지 않으면 m.left가 None일 때 에러 발생 가능.
            if m.left:
                m.left.parent = m.parent
            # m이 최대라 m의 오른쪽 부트리는 없음.
            m.right = r
            m.left = l
            l.parent = m
            if r:
                r.parent = m
            replace = m
            
        if self.root == x:
            if replace:
                replace.parent = None
            self.root = replace
        else:
            if p.left == x:
                p.left = replace
            else:
                p.right = replace
            if replace:
                replace.parent = p
        self.size -= 1
    # O(h)
        
    # 연산들이 O(h)이니 높이가 중요 (높이 등의 조건을 강제적으로 유지하도록 하는 것 -> balanced binary search tree)



B = BinarySearchTree()
B.insert(25)
B.insert(5)
B.insert(53)
B.insert(1)
B.insert(6)
B.insert(27)
B.insert(67)
B.insert(26)
B.insert(28)
B.insert(29)
B.preorder(B.root)
print()
B.inorder(B.root)
print()
B.deleteByCopying(B.search(53)) # copying 방식 delete
B.deleteByMerging(B.search(29)) # merging 방식 delete
B.preorder(B.root)
print()
B.inorder(B.root)
print()
#      25          =>         25
#     /   \        =>        /  \
#    5    53       =>       5   27
#   / \   / \      =>      /\    /\
#  1  6  27 67     =>     1  6  26 28
#       / \        =>                \
#      26 28       =>                 67
#           \
#           29