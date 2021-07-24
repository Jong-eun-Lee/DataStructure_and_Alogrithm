## DynamicArray(동적 배열)
# 작성자: 이종은

import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0 # 가지고 있는 원소 개수.
        self.capa = 1 # capacity의 default 값은 1로 해줌.
        self.A = self.makeArray(self.capa)

    def __len__(self):
        return self.n

    def makeArray(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError("Invalid index")
        return self.A[index]
    
    def append(self, new):
        if self.n == self.capa:
            self.resize(2 * self.capa) # capa 꽉 차면 2배로 늘려줌.
        self.A[self.n] = new # 배열 끝에 새로운 값 넣어주기.
        self.n += 1

    def resize(self, capacity):
        B = self.makeArray(capacity)
        for e in range(self.n):
            B[e] = self.A[e]
        self.A = B
        self.capa = capacity
        # 기존 배열 A에서 size를 늘려준 B로 이사.
    
    def insert(self, k, val):
        if self.n == self.capa:
            self.resize(2 * self.capa)
        for i in range(self.n, k, -1):
            # [n-1]부터 [k]까지의 원소를 [n]부터 [k+1]까지로 밀려나 이동.
            # 넣으려는 원소는 A[k]에.
            self.A[i] = self.A[i-1]
        self.A[k] = val
        self.n += 1

    def remove(self, val):
        for k in range(self.n):
            if self.A[k] == val:
                for i in range(k, self.n - 1):
                    self.A[i] = self.A[i + 1]
                # [k+1]부터 [n-1]까지의 원소를 [k]부터 [n-2]까지로 당겨서 이동.
                self.A[self.n - 1] = None
                self.n -= 1
                return
        raise ValueError("The value is not found")

    def reverse(self):
        for k in range(self.n//2):
            self.A[self.n - 1 - k], self.A[k] = self.A[k], self.A[self.n - 1 - k]

    def extend(self, otherArray): # 다른 배열을 기존 배열에 붙이기
        newSize = self.n + len(otherArray)
        growingRate = 1
        while newSize > (growingRate * self.capa):
            growingRate *= 2
        if growingRate > 1: # growingRate가 여전히 1이면 용량이 충분해서 resize 안 해줌.
            self.resize(growingRate * self.capa)
        for e in otherArray:
            self.A[self.n] = e
            self.n += 1

    def pop(self):
        if self.n < self.capa // 4:
            self.resize(self.capa // 2)
        # 원소 개수가 capacity의 1/4보다 작아지면
        # capacity를 반으로 줄여줌.
        e = self.A[self.n - 1]
        self.A[self.n - 1] = None
        self.n -= 1
        return e
    
    def __repr__(self):
        array = " | ".join(str(self.A[i]) for i in range(self.n))
        return "| " + array + " |"

array1 = DynamicArray()
for i in range(1, 6):
    array1.append(i)
print("array1:", array1)

array2 = DynamicArray()
for i in range(6, 11):
    array2.append(i)

print("array2:", array2)

array1.extend(array2)
print("array extended:", array1)

array1.reverse()
print("array reversed:", array1)

print(array1.n, array1.capa, array2.n, array2.capa)