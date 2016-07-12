from radon.complexity import cc_visit
from radon.raw import analyze


def equi(A, N):
    lsum = 0
    rsum = sum(A)

    for i in range(N):
        rsum -= A[i]
        if lsum == rsum:
            yield i
        lsum += A[i]
    return -1

testdata = [-1, 3, -4, 5, 1, -6, 2, 1]
print(list(equi(testdata, len(testdata))))

