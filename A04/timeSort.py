"""
PROBLEM 4
The file helps us time how long it takes to bubble sort a list. This file generates a random list of size n. We import pySort to
sort this list. In this file we check the time it takes to sort a list of size 10^3, 10^4, 10^5, and 10^6
"""
import pySort
from time import perf_counter
import random

def generateListToSort(n):
    A = list(0 for i in range(n))
    for i in range(n):
        A[i] = random.randint(0,1000)
    return A

n_1 = 10**3
n_2 = 10**4
n_3 = 10**5
n_4 = 10**6
A_1 = generateListToSort(n_1)
A_2 = generateListToSort(n_2)
A_3 = generateListToSort(n_3)
A_4 = generateListToSort(n_4)

print("First element before sorting " + str(n_1) + " elements: " + str(A_1[0]))

t_start_1 = perf_counter()
A_1 = pySort.sorter(A_1)
t_stop_1 = perf_counter()

print("Time elasped is: " + str(t_stop_1 - t_start_1) + " seconds")
print("First element after sorting " + str(n_1) + " elements: " + str(A_1[0]))

print("\n")

print("First element before sorting " + str(n_2) + " elements: " + str(A_2[0]))

t_start_2 = perf_counter()
A_2 = pySort.sorter(A_2)
t_stop_2 = perf_counter()

print("Time elasped is: " + str(t_stop_2 - t_start_2) + " seconds")
print("First element after sorting " + str(n_2) + " elements: " + str(A_2[0]))

print("\n")

print("First element before sorting " + str(n_3) + " elements: " + str(A_3[0]))

t_start_3 = perf_counter()
A_3 = pySort.sorter(A_3)
t_stop_3 = perf_counter()

print("Time elasped is: " + str(t_stop_3 - t_start_3) + " seconds")
print("First element after sorting " + str(n_3) + " elements: " + str(A_3[0]))

print("\n")

print("First element before sorting " + str(n_4) + " elements: " + str(A_4[0]))

t_start_4 = perf_counter()
A_4 = pySort.sorter(A_4)
t_stop_4 = perf_counter()

print("Time elasped is: " + str(t_stop_4 - t_start_4) + " seconds")
print("First element after sorting " + str(n_4) + " elements: " + str(A_4[0]))

print("\n")


