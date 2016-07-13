A = [2, -2, 3, 0, 4, -7]

def solution(A):
    # write your code in Python 2.7
    for i in range(0, len(A)-1):
        for p in range(1, len(A)):
            pas = p + 1
            if i < pas:
                tmp = sum(A[i:pas])
                print("DEBUG: (%d, %d)" % (i, pas-1))
                if tmp == 0:
                    yield (i, pas-1)


def solutiona(A):
    # write your code in Python 2.7
    result = list()
    for i in range(0, len(A)-1):
        for p in range(1, len(A)):
            pas = p + 1
            if i < pas:
                tmp = sum(A[i:pas])
                if tmp == 0:
                    result.append((i, pas-1))
    return result if result else -1

print(solutiona(A))