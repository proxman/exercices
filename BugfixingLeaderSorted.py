import random
from unittest import TestCase
from ref import leaders

def solution(A):
    n = len(A)
    L = [-1] + A
    count = 0
    pos = (n // 2) + 1
    candidate = L[pos]
    for i in range(1, n + 1):
        if (L[i] == candidate):
            count = count + 1
    if (count >= pos):
        return candidate
    return -1

A = [2, 2, 2, 2, 2, 2, 4, 4, 4, 4]
B = [1, 1, 1, 1, 3, 3, 6, 6]
C = [5, 9, 9]
D = [5, 6, 6, 9, 9, 9]



print(leaders(D))
print(solution(D))

def genlist():
    batch = random.randint(2, 5)
    alist = list()
    for _ in range(batch):
        num = random.randint(1, 10)
        times = random.randint(1, 10)
        alist.extend([num] * times)
    return sorted(alist)

C = genlist()

for i in range(50):
    alist = genlist()
    l = leaders(alist)
    s = solution(alist)
    if s != l:
        print('======%d=======' % i)
        print(alist)
        print("Leader: %d" % l)
        print("Solution: %d" % s)
        print('===============')


