## HashFunction(해시 함수)
# 작성자: 이종은

# Hash Table은 삽입, 삭제, 탐색 연산이 평균적으로 상수 시간에 가능.
# Hash table의 slot(bucket)에 key와 value의 쌍을 저장. 해시 함수 f(key)에 따라 key 값을 slot에 mapping.
# slot에 mapping 했는데, 어떤 값이 이미 있는 경우 충돌(collision)이 발생했다고 함.
# 충돌이 발생할 경우 해결하는 방법 -> Collision Resolution Method.

# Hash Table 요소 세 가지: 1. table(리스트로 관리하겠음) 2. hash function 3. collision resolution method
# m은 해시 테이블의 사이즈(슬롯의 개수)

# 해시 함수의 종류.
# perfect hash function(완전 해시 함수): 충돌 없이 일대일로 매핑하는 해시 함수.
# c-universal hash function: Pr(f(x) == f(y)) = c/m. 서로 다른 key 값의 충돌이 발생할 확률이 c/m.
# c가 1일 경우 universal hash function or 1-universal hash function

# 좋은 hash function이란? 1. 충돌이 적어야 함 2. 해시 함수 값의 계산이 빨라야 함.
# 하지만 이 두 가지는 trade-off 관계에 있음. 충돌이 적게 하려면 해시 함수가 복잡해져 계산이 느려지고, 해시 함수 계산을 빨리 하려고 하면 어느 정도 충돌은 감수해야 함. 그러므로 적절하게 균형을 맞춰서 효율적인 해시 함수 만들어야 함.

# 해시 함수의 예: division, folding, mid-square, ...

# key가 string일 때 해시 함수
# p는 prime number. m은 slot 개수(해시 테이블의 size)
def additiveHash(key, p, m):
    h = initialValue
    for i in range(len(key)):
        h += key[i]
    return h % p % m

def rotatingHash(key, p, m):
    h = initialValue
    for i in range(len(key)):
        h = (h << 4) ^ (h >> 28) ^ key[i]
    return h % p % m

def universalHash(key, a, p, m):
    h = initialValue
    for i in range(len(key)):
        h = ((h*a) + key[i]) %p
    return h % m