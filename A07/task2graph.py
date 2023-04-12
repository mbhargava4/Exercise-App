import numpy as np
import sys
import argparse
import random
from time import perf_counter
import matplotlib.pyplot as plt

size = [2**10, 2**11,2**12,2**13]
t = [1.34, 5.06, 20.237, 696.695]
fig, ax = plt.subplots()
x = (size)
y = (t)


ax.set_xlabel('Size (n)')
ax.set_ylabel('Time (ms)')



plt.plot(x,y, 'b-', label ='Time comparsion task 2')
plt.show()
