## Red-Black Tree
# 작성자: 이종은
# 구현 코드 별도 첨부

# 레드 블랙 트리에선 None 노드, 즉 NIL 노드를
# 독립된 노드로 취급함.
# 그리고 NIL 노드는 모두 리프 노드로 간주함.
# 리프 노드 외에 다른 나머지 노드를 내부 노드라고 함.

# 5개 조건을 만족하는 BST를 레드 블랙 트리라 함.
# 1. 모든 노드는 red나 black 색깔을 가져야 함.
# 2. root 노드는 black이어야 한다.
# 3. leaf(NIL 노드)는 black이어야 한다.
# 4. red node는 두 개의 자식 노드를 갖는데, 그 자식 노드 모두 black.
# (black 노드의 자식은 레드일 수도 있고, 블랙일 수도 있고)
# 5. !!! 특정 노드에서 leaf node들로 향하는 모든 경로의
# black 노드 개수가 다 동일해야 한다.
# h(v) = v의 높이
# bh(v) = v는 제외 하고 v에서 리프 노드로 가면서 만나는 블랙 노드의 개수

# 사실 1: # v의 subtree의 내부 노드 개수(리프 노드 개수를 뺀)
# >= 2^(bh(v)) - 1

# 사실 1 증명: h(v)에 대한 귀납법(induction)

# Base case 먼저 증명해야
# Base case: h(v) = 0 (리프 노드 하나 밖에 없다는 것) (블랙 하나)
# => bh(v) = 0 (참)

# Hypothesis. 가정 단계
# H: h(v) <= k면 v의 subtree의 내부노드 개수 >= 2^(bh(v)) - 1
# 가 성립한다고 가정

# Induction 단계
# I: h(v) = k+1 일 때 사실 1이 성립함을 증명해야.

#          v
#       w    z
#       L    R
#
# h(v) = k+1이라 했으니 h(w) <= k, h(z) <= k 일 것
# h(w) <= k라고 했으니 가정을 이용할 수 있음.
# L(w의 subtree)의 내부노드 개수는 >= 2^(bh(w)) - 1
# R의 내부노드 개수 >= 2^(bh(z)) - 1
# 그래서 v의 subtree 내부 노드 개수
# >= 2(bh(w)) - 1 + 2^(bh(z)) - 1 + 1
# 마지막 1은 v 자신

# 이제 bh(w), bh(z) 값이 관건
# bh(w), bh(z) = bh(v) or bh(v) - 1
# bh(w), bh(z) >= bh(v) - 1

# w가 red라고 하면
# v의 입장에서 bh 세나 w 입장에서 세나 똑같
# bh(w) = bh(v)

# w가 검정색이라고 하면
# bh(w) = bh(v) - 1

# v의 subtree의 내부 노드 개수
# >= 2 * 2^(bh(v)-1) - 1
# = 2^(bh(v)) - 1
# 증명.

# 사실 2: black 노드 수 >= h/2
# bh(root) >= h/2
# 루트 노드부터 리프 노드까지 노드 수 셀 때 레드가 더 많을 순 없기에.
# root의 subtree의 내부노드 개수
# >= 2^(bh(root)) - 1
# >= 2^(h/2) - 1
# n >= 2^(h/2) - 1
# 2^(h/2) <= n + 1
# h <= 2 * log(n+1)
# ∴ h = O(log n)

## Red-Black Tree 삽입 연산
# 1. BST의 insert 호출해 새로운 노드 x 삽입
# 2. x.color = red
# 3. 4가지 case에 따라 조정.

# case 1: x = T.root 인 경우
# x.color = black

# case 2: x.parent.color == black
# 그대로 놔둠.

# case 3: x.parent.color == red
# case 3-1: x.uncle.color = red 인 경우
# x의 grandparents는 black일 것
# => 조부모는 레드, 부모와 삼촌은 블랙으로 바꿔 줘야 함.
# case 3-2: x.uncle.color = black 인 경우
#   case 3-2-1: x - p - g가 linear한 경우
#   g에서 1번 회전 후 색깔 재배치(x와 g는 같은 레벨에서 레드, p는 x와 g를 자식으로 둔 블랙) 
#   case 3-2-2: x - p - g가 left-right나 right-left인 경우(삼각형)
#   2번 회전 후 색깔 재배치(p와 g는 같은 레벨에서 레드, x는 p와 g를 자식으로 둔 블랙)

# insert: 회전 최대 2번 + 색깔 조정 (회전과 색깔 조정은 O(1))
# O(log n) 

# delete도 O(log n)

# AVL: insert에서 회전 최대 두 번. delete에서 최악의 경우 회전 O(log n) 번.
# Red-Black: insert에서 회전 최대 두 번. delete에서 회전 3번 필요.

# delete 연산을 비교했을 때 Red-Black tree가 더 좋음.