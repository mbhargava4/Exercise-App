import random
import pyMatmul
from time import perf_counter

def generateRandomMatrix(n):
    C=[list(0 for i in range(n)) for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = random.randint(0,9)

    return C

n=2**9
print("number of elements " + str(n))
A = generateRandomMatrix(n)
B = generateRandomMatrix(n)

t_start = perf_counter()
C = pyMatmul.Matmul(A,B)
t_stop = perf_counter()

print("time elasped for this program is " + str(t_stop- t_start))



