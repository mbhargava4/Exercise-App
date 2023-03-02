import pyMatmul
import numpy as np 
import sys
import argparse
import random
from time import perf_counter
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()

parser.add_argument('-P', '--PLOTLINE', type=float, default =1)

args = parser.parse_args()
if(args.PLOTLINE==0):
    plotbool = False
else:
    plotbool = True


#function to generate random matrix of nxn size
def generateRandomMatrix(n):
    C=[list(0 for i in range(n)) for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = random.randint(-1,1) #numbers in this matrix are between -1 and 1

    return C

k = [5,6,7]
size = list(0.0 for i in range(4))
t = list(0.0 for i in range(4))
t_1 = list(0.0 for i in range(4))

for i in k:
   
    n=2**(i)
    size[i-5] = n
    A_list = generateRandomMatrix(n)
    B_list = generateRandomMatrix(n)
    
    A=np.zeros([n,n])
    B=np.zeros([n,n])
    for a in range(n):
        for b in range(n):
            A[a][b]=A_list[a][b]
            B[a][b]=B_list[a][b]
    
    t_start_1 = perf_counter()
    C_list = pyMatmul.Matmul(A_list,B_list)
    t_stop_1 = perf_counter()
    time = (t_stop_1 - t_start_1)*1000
    t[i-5] = time
    
    t_start_2 = perf_counter()
    C=A@B
    t_stop_2 = perf_counter()
    t_1[i-5] = (t_stop_2 - t_start_2)*1000
    


n=2**8
size[3]=n
A_list = generateRandomMatrix(n)
B_list = generateRandomMatrix(n)
    
A=np.zeros([n,n])
B=np.zeros([n,n])
for i in range(n):
    for j in range(n):
        A[i][j]=A_list[i][j]
        B[i][j]=B_list[i][j]
    
t_start_1 = perf_counter()
C_list = pyMatmul.Matmul(A_list,B_list)
t_stop_1 = perf_counter()
t[3] = (t_stop_1-t_start_1)*1000


t_start_2 = perf_counter()
C=A@B
t_stop_2 = perf_counter()
t_1[3] = (t_stop_2-t_start_2)*1000
print(str(C_list[0][0]) + "\n" + str(t[3]) + "\n" + str(C[0][0]) + "\n" + str(t_1[3]))

fig, ax = plt.subplots()

x = (size)
y = (t)
y_1 = (t_1)
ax.set_xscale('log', base=2)
ax.set_xlabel('Size (n)')
ax.set_yscale('log', base=10)
ax.set_ylabel('Time (ms)')
ax.set_title('Time vs size plot for multipliying matrices')


if(plotbool):
    plt.plot(x,y, 'b-', label ='pyMatmul')
    plt.plot(x,y_1, 'g-', label = 'numpy')
    plt.legend()
    plt.show()

