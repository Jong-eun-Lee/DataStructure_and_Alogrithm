## AVL Tree
# 작성자: 이종은

#===========================================================================================#
## Balanced BST (균형 이진 탐색 트리)
# 작성자: 이종은
# 이진 탐색 트리의 높이 범위는 log(n+1) - 1 <= h <= n-1 과 같은데,
# 조정 등을 통해 n개의 노드가 저장된 BST의 h를 항상 O(log n)으로 유지하는 것이
# '균형 이진 탐색 트리(balanced binary search tree)'

# 삽입, 삭제 연산 등을 통해 트리의 높이가 높아지면 O(log n)을 유지하기 위한 조정이 필요하다.
# 조정은 Rotation(회전)을 통해 이루어진다(한 번 혹은 여러 번의 회전을 통해).
# ex) z 입장에서 x의 왼쪽 부트리 A의 높이가 높으면 right rotation을 통해 조정.
#      z
#    x   C
#  A  B
# A < x < B < z < C (이 성질을 유지하면서 회전해야 함)
#    z's parent
#              x
#            A   z
#               B  C
# z를 기준으로 right rotation 하면 (right rotation at z)
# 위와 같이 z는 오른쪽으로 내려가고 x가 위쪽으로. B은 x가 아닌 z에 붙음.
# x와 A는 올라가면서 한 레벨 줄어듦
# z와 C는 내려가면서 한 레벨 늘어남.
# B는 똑같은 레벨.
# z.parent.child = x
# x.parent = z.parent
# x.right = z
# z.parent = x
# z.left = B
# B.parent = z

#===========================================================================================#

## AVL Tree (Adelson-Velsky & Landis, 1962)
# 모든 노드에 대해서 노드의 왼쪽 부트리와 오른쪽 부트리의 높이 차가 1이하인 BST.
# 그러면 이 조건을 만족하면 항상 높이가 O(log n)이 되는가?
# 증명(높이가 h이고 노드 개수가 n인 AVL tree가 h <= c*(log2 n) 임을):
# h = 0 최소 노드 수 1
# h = 1 최소 노드 수 2
# h = 2 최소 노드 수 4
# h = 3의 최소 노드 수 예시 (4 + 2 + 1)
#        o
#     o     o
#   o  o   o
# o 
# 루트 노드의 왼쪽엔 높이가 2인 최소 노드의 AVL tree가 붙고,
# 루트의 오른쪽엔 높이가 1인 최소 노드의 AVL tree가 붙어 있다.


# 높이가 h인 AVL tree 중 최소 노드 개수를 Minh라고 하면
# Min0 = 1
# Min1 = 2
# Min2 = 4
# Min3 = 7
# Min4 = 12
# Minh = 1 + Min(h-1) + Min(h-2) > 1 + 2*Min(h-2)
# > 2*Min(h-2) = 2*(1+ Min(h-3) + Min(h-4))
# > 2*(2*Min(h-4)) = 2^2(Min(h-4))
# > 2^(h/2) * Min0 # Min 0까지 가려면 2를 h/2번 빼줌 (h가 짝수일 때)
# = 2^(h/2)
# ∴ Min(h) >= 2^(h/2)

# 2^(h/2) <= Minh <= n
# h/2 <= log2 n  
# h <= 2 * log n
# ∴ h = O(log n)


class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0
    
    def __str__(self):
        return str(self.key)

    def __iter__(self): # inorder 방식으로
        if self:
            if self.left:
                for e in self.left:
                    yield e
            yield self.key
            if self.right:
                for e in self.right:
                    yield e
    
    def leftHeight(self):
        if self.left:
            return self.left.height
        return -1 # 존재하지 않는 노드의 높이는 -1로 함.
        # 자식이 없는 노드의 높이를 max(-1, -1) + 1
        # 즉 0으로 계산할 수 있어 make sense.

    def rightHeight(self):
        if self.right:
            return self.right.height
        return -1

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __iter__(self):
        return self.root.__iter__()
    
    def __str__(self):
        return " - ".join(str(key) for key in self)
    
    def __contains__(self, key): # key가 존재한다면 True, 그렇지 않으면 False 반환
        return self.search(key) != None
    
    def preorder(self, v):
        if v:
            print(v, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)
        
    def inorder(self, v):
        if v:
            self.inorder(v.left)
            print(v, end=" ")
            self.inorder(v.right)
    
    def postorder(self, v):
        if v:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v, end=" ")
    
    def search(self, key):
        p = self.findLocation(key)
        if p and p.key == key:
            return p
        else: return None
    
    def findLocation(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p # 매칭되는 key가 없다면 key가 들어갈 수 있는 자리의 부모 노드를 return

    def insert(self, key):
        p = self.findLocation(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
            self.size += 1
            self.updateHeight(v)
            return v
        else:
            print("The key is already in tree.")
            return p
    
    def deleteByCopying(self, x):
        if x == None:
            return None
        a = x.left
        if a == None:
            b, p = x.right, x.parent
            if p == None:
                self.root = b
            else:
                if p.left == x:
                    p.left = b
                else:
                    p.right = b
            if b:
                b.parent = p
            del x
        else:
            m = a # m은 a 부트리 중 가장 큰 것
            while m.right:
                m = m.right
            x.key = m.key
            l, p = m.left, m.parent
            if p.left == m:
                p.left = l
            else:
                p.right = l
            if l:
                l.parent = p
            del m
        self.size -= 1
        self.updateHeight(p)
        return p # x를 채우기 위해 빠져나간 m의 본래 부모 노드를 return.
    
    def deleteByMerging(self, x):
        if x == None:
            return None
        a, b, p = x.left, x.right, x.parent
        if a == None:
            replace = b
            s = p
        else:
            replace = m = a # replace와 m은 일단 a로
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m
            s = m
        if self.root == x:
            if replace:
                replace.parent = None
            self.root = replace
        else:
            if p.left == x:
                p.left = replace
            else:
                p.right = repalce
            if replace:
                replace.parent = p
        del x
        self.size -= 1
        self.updateHeight(s)
        return s
    
    def height(self, x):
        if x == None:
            return -1
        return x.height
    
    def updateHeight(self, v):
        while v != None:
            l, r = -1, -1
            if v.left:
                l = v.left.height
            if v.right:
                r = v.right.height
            v.height = max(l, r) + 1
            v = v.parent
    
    #  z.p     =>    z.p
    #   z      =>     x
    # a   x    =>   z   c
    #    b c   =>  a b
    def rotateLeft(self, z):
        if z == None: return
        x = z.right
        if x == None: return
        b = x.left
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            if z.parent.right == z:
                z.parent.right = x
        x.left = z
        z.parent = x
        z.right = b
        if b:
            b.parent = z
        if self.root == z:
            self.root = x
        self.updateHeight(z)

    def rotateRight(self, z):
        if z == None: return
        x = z.left
        if x == None: return
        b = x.right
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            if z.parent.right == z:
                z.parent.right = x
        x.right = z
        z.parent = x
        z.left = b
        if b:
            b.parent = z
        if self.root == z:
            self.root = x
        self.updateHeight(z)

class AVLtree(BST):
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isBalanced(self, v):
        return abs(v.leftHeight() - v.rightHeight()) <= 1
    
    # rebalance case는 총 네 가지(z가 unbalanced 하다고 하자).
    # right-right case solved by "rotateLeft at z"
    #     z            ->       y
    #  T1    y         ->    z      x
    #     T2   x       ->  T1 T2  T3 T4
    #        T3 T4     ->
    # (left-left case는 rotateRight로 해결)
    # right-left case solved by rotateRight at y and "rotateLeft at z"
    #      z       ->        z             ->       x
    #  T1     y    ->    T1      x         ->   z      y
    #       x  T4  ->         T2    y      -> T1 T2  T3 T4
    #     T2 T3    ->             T3  T4   ->
    # (left-right case는 rotateLeft at y 후 rotateRight at z로 해결)
    def rebalance(self, x, y, z):
        # rebalance 후 x, y, z 중 맨 위인 z 자리에 오는 노드 return
        print(f"Rebalance at {z}, {y}, {x}")
        if z.left == y and y.left == x: # left-left case
            self.rotateRight(z)
            return y
        elif z.right == y and y.right == x:
            self.rotateLeft(z)
            return y
        elif z.left == y and y.right == x: # left-right case
            self.rotateLeft(y)
            self.rotateRight(z)
            return x
        elif z.right == y and y.left == x:
            self.rotateRight(y)
            self.rotateLeft(z)
            return x
    
    def isavl(self, v):
        if v == None: return True
        return self.isBalanced(v) and self.isavl(v.left) and self.isavl(v.right)
    
    def isAVL(self):
        return self.isavl(self.root)
    
    def insert(self, key):
        v = super(AVLtree, self).insert(key)
        x, y, z = v, v.parent, None
        while y:
            z = y.parent
            if z and self.isBalanced(z):
                x, y = y, z
            else:
                if z:
                    self.rebalance(x, y, z)
                break
        return v
    
    def delete(self, u):
        v = self.deleteByCopying(u)
        while v:
            if not self.isBalanced(v):
                z = v
                if z.leftHeight() >= z.rightHeight():
                    y = z.left
                else:
                    y = z.right
                if y.leftHeight() >= y.rightHeight():
                    x = y.left
                else:
                    x = y.right
                v = self.rebalance(x, y, z)
            v= v.parent


a = AVLtree()
a.insert(25)
a.insert(5)
a.insert(53)
a.insert(1)
a.insert(6)
a.insert(27)
a.insert(67)
a.insert(26)
a.insert(28)
a.insert(29)
a.insert(30)
a.delete(a.search(30))

a.preorder(a.root)
print()
a.inorder(a.root)
print()
#           28
#         /    \
#       25      53
#      / \      / \
#    5    27   29 67
#   / \   /
#  1  6  26
print(a.height(a.root))
print(a.isBalanced(a.root))