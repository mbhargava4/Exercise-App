"""
PROBLEM 3
This file contains the code that will help us multiply 2 matrices. It uses nested for loops to get the job done.
"""

def matmul(A,B):
    n = len(A) #I have assumed that the matrices A and B are of the same size and each of them is in nxn format. 
    C=[list(0 for i in range(n)) for j in range(n)] #Creates a matrix of nxn size which has all its values as zero 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j] #initial value of C[i][j]=0, so adding all the other values should give us the number we need
    return C #returns desired Matrix 

#This is a test I made to see if it works, please ignore
# A = [[1,2,3],[2,3,4],[3,4,5]]
# B = [[2,3,4],[3,-6,5],[4,5,6]]
# C=Matmul(A,B)
# print(C)