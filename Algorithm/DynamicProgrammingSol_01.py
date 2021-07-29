# 작성자: 이종은
## 2021-05-07 작성

# Q1)
mn = list(map(int, input().split()))
m = mn[0]
n = mn[1]
c = []
from collections import deque
deq = deque(c)
for i in range(m):
		deq.appendleft(list(map(int, input().split())))
		# list 함수의 inset(0, val)을 쓰는 것보다 성능이 좋을 것.
C = list(deq)
if m <= n: # 행의 개수보다 열의 개수가 더 많거나 같을 때(가로가 더 길거나 같을 때)
	# 테이블의 크기는 O(m)이다.
	table = [C[0][0]]
	# 테이블을 세로줄 한 줄이라 생각하고 푼다.
	for i in range(1, m):
		table.append(C[i][0] + table[i-1])
		# 첫 번째 열을 기준으로 위로 가면서 비용을 더 해줘 초기 테이블 형성
	if n >= 2:
		for i in range(1, n):
			for j in range(0, m):
				if j == 0:
					table[j] = C[j][i] + table[j]
				else:
					table[j] = C[j][i] + min(table[j-1], table[j])

if m > n: # 행의 개수가 열의 개수보다 많을 때
	table = [C[0][0]]
	for i in range(1, n):
		table.append(C[0][i] + table[i-1])
	if m >= 2:
		for i in range(1, m):
			for j in range(0, n):
				if j == 0:
					table[j] = C[i][j] + table[j]
				else:
					table[j] = C[i][j] + min(table[j-1], table[j])

print(table[-1])



# Q2)
mn = list(map(int, input().split()))
m = mn[0]
n = mn[1]
c = []
from collections import deque
deq = deque(c)
for i in range(m):
		deq.appendleft(list(map(int, input().split())))
		# list 함수의 inset(0, val)을 쓰는 것보다 성능이 좋을 것.
C = list(deq)

table = []

for i in range(n):
	table.append(C[0][i])
		#초기 테이블 설정(맨 아래 행을 초기 테이블로 해줌)

temp = [0] * n
	# 테이블을 갱신시켜 주고 나면 왼쪽 아래쪽 대각선에 있는 걸
	# 참조하지 못할 수 있기 때문에 왼쪽 아래쪽 대각선에 있는 걸 따로
	# temp 리스트에 저장해준다.
	# 예를 들어 table[2]를 갱신해주려면 table[1], table[2], table[3]을 고려하면
	# 안 되는 것이다. 왜냐하면 table[1]이 이미 갱신되어 왼쪽 아래 값을 제대로
	# 참조할 수 없기 때문이다. 그래서 table[1]을 갱신해주기 전에
	# temp[1]에 table[1] 값을 저장해준다. 그리고 나서 table[2]를 갱신할 때
	# temp[1], table[2], table[3]에서 작은 것을 고른 후 그 자리의 비용과 더해준다.
for i in range(1, m):
	for j in range(0, n):
		if j == 0: # 맨 왼쪽 열에 대해
			temp[j] = table[j]
			if n == 1: # 열 개수가 하나일 때
				table[j] = C[i][j] + table[j]
			else: # 열 개수가 두 개 이상일 때
				table[j] = C[i][j] + min(table[j], table[j+1])

		elif j != 0 and j != n-1:
			temp[j] = table[j]
			table[j] = C[i][j] + min(temp[j-1], table[j], table[j+1])

		elif j == n-1: # 맨 오른쪽 열에 도달했을 때
			table[j] = C[i][j] + min(temp[j-1], table[j])

print(min(table)) # 맨 위의 행에 도달했을 때 비용의 총합이 최소인 것을 선택한다.