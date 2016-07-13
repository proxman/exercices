D = [10, 11, 12]
C = [1,2,3,4,5,6,7,8,9,10]
A = [1,3,2,1]
B = [4,2,5,3,2]

def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        if i < len(B) - 1 and B[i] < a:
            i += 1
        if a in B:
            return a
    return -1


print(solution(D, C))