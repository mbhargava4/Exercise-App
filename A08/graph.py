import numpy as np
import matplotlib.pyplot as plt


n = [7,8,9,10,11,12]
t1 = [0.00000, 0.00000, 0.00000, 0.001000, 0.002000, 0.00300]
t2 = [0.00000, 0.00000, 0.00000, 0.001000, 0.00100, 0.001000]

plt.plot(n, t1, label='sumArray1')
plt.plot(n, t2, label='sumArray2')
plt.xlabel('n')
plt.ylabel('Time (ms)')
plt.xscale('log')
plt.yscale('linear')
plt.legend()
plt.show()