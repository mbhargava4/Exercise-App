import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

n_values = [2**i for i in range(10, 14)]
t_values = []

for n in n_values:
    A = np.random.uniform(-1, 1, (n, n))
    b = np.ones(n)
    start = perf_counter()
    c = np.zeros(n)
    for i in range(n):
        for j in range(n):
            c[i] += A[i][j] * b[j]
    end = perf_counter()
    t = (end - start) * 1000
    t_values.append(t)

plt.semilogx(n_values, t_values)
plt.xlabel('n')
plt.ylabel('time (ms)')
plt.title('Python Matrix-Vector Multiplication')
plt.show()