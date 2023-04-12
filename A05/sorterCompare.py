from pySort import sorter
import numpy as np
import sys
import argparse
import random
from time import perf_counter
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()

parser.add_argument('-P', '--PLOTLINE', type=float, default=1)

args = parser.parse_args()
if (args.PLOTLINE == 0):
    plotbool = False
else:
    plotbool = True


def generateListToSort(n):
    A = list(0 for i in range(n))
    for i in range(n):
        A[i] = random.randint(-10, 10)
    return A


k = [10, 11, 12, 13, 14]
size = list(0.0 for i in range(len(k)))
t = list(0.0 for i in range(len(k)))
t_1 = list(0.0 for i in range(len(k)))
t_2 = list(0.0 for i in range(len(k)))
C_list = list(0.0 for i in range(2**14))
D_list = list(0.0 for i in range(2**14))
C = list(0.0 for i in range(2**14))

for i in k:
    n = 2**i
    size[i-10] = n
    A_list = generateListToSort(n)

    B_list = list(0 for i in range(n))
    for j in range(n):
        B_list[j] = A_list[j]

    A = np.zeros(n)
    for j in range(n):
        A[j] = A_list[j]

    t_start_1 = perf_counter()
    C_l = sorter(A_list)
    t_stop_2 = perf_counter()
    t[i-10] = (t_stop_2-t_start_1)*1000
    if (i==14):
        C_list = C_l

    t_start_2 = perf_counter()
    B_list.sort()
    t_stop_2 = perf_counter()
     
    t_1[i-10] = (t_stop_2-t_start_2)*1000
    if(i==14):
        D_list = B_list

    t_start_3 = perf_counter()
    C_n = np.sort(A)
    t_stop_3 = perf_counter()
    t_2[i-10] = (t_stop_3-t_start_3)*1000
    C = C_n


print(str(C_list[0]) + "\n" + str(t[4]) + "\n" + str(D_list[0]) + "\n" + str(t_1[4]) +  "\n" + str(C[0]) + "\n" + str(t_2[4]))

fig, ax = plt.subplots()
x = (size)
y = (t)
y_1 = (t_1)
y_2 = (t_2)
ax.set_xscale('log', base=2)
ax.set_xlabel('Size (n)')
ax.set_yscale('log', base=10)
ax.set_ylabel('Time (ms)')
ax.set_title('Time vs size plot for sorting 1D matrix')


if(plotbool):
    plt.plot(x,y, 'b-', label ='pySort')
    plt.plot(x,y_1, 'g-', label = 'sort')
    plt.plot(x,y_2, 'r-', label = 'numpy')
    plt.legend()
    plt.show()