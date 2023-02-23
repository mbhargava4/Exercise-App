def sorter(A):
    C=A[:]
    n = len(A)
    for j in range(n-1):
        for i in range(n-j-1):
            if(C[i]>C[i+1]):
                temp = C[i]
                C[i] = C[i+1]
                C[i+1]=temp
          
    return C

# A = [12, 45, 23, 51, 19, 8]
# print(A)
# C = sorter(A)
# print(sorter(A))