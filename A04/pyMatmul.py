
def Matmul(A,B):
    n = len(A)
    C=[list(0 for i in range(n)) for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    return C

# A = [[1,2,3],[2,3,4],[3,4,5]]
# B = [[2,3,4],[3,-6,5],[4,5,6]]
# C=Matmul(A,B)
# print(C)