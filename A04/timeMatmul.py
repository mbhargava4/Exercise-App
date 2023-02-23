"""
PROBLEM 3
This file helps us find out the time is takes for the code to multiply 2 matrices. We import pyMatmul to multiply the matrices. 
This file also generates 2 random matrices of nxn size. This file checks the time it takes to multiply 2 matrices of nxn size where n
is 2^7, 2^8, and 2^9.
"""
import random
import pyMatmul
from time import perf_counter

#function to generate random matrix of nxn size
def generateRandomMatrix(n):
    C=[list(0 for i in range(n)) for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = random.randint(0,9) #numbers in this matrix are between 0 and 9

    return C

n_1=2**7
print("number of elements " + str(n_1))
A_1 = generateRandomMatrix(n_1)
B_1 = generateRandomMatrix(n_1)

t_start_1 = perf_counter()
C_1 = pyMatmul.Matmul(A_1,B_1)
t_stop_1 = perf_counter()

print("time elasped to multiply a " + str(n_1) + " x " + str(n_1) + " is " + str(t_stop_1- t_start_1))

print('\n')

n_2=2**8
print("number of elements " + str(n_2))
A_2 = generateRandomMatrix(n_2)
B_2 = generateRandomMatrix(n_2)

t_start_2 = perf_counter()
C_2 = pyMatmul.Matmul(A_2,B_2)
t_stop_2 = perf_counter()

print("time elasped to multiply a " + str(n_2) + " x " + str(n_2) + " is " + str(t_stop_2 - t_start_2))
print('\n')

n_3=2**9
print("number of elements " + str(n_3))
A_3 = generateRandomMatrix(n_3)
B_3 = generateRandomMatrix(n_3)

t_start_3 = perf_counter()
C_3 = pyMatmul.Matmul(A_3,B_3)
t_stop_3 = perf_counter()

print("time elasped to multiply a " + str(n_3) + " x " + str(n_3) + " is " + str(t_stop_3 - t_start_3))

