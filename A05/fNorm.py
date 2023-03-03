import numpy as np
import sys
import csv

file_name = sys.argv[1]

with open(file_name + ".csv") as file:
    csvreader = csv.reader(file, delimiter = "\t")

    for matrix in csvreader:
        for i in range(matrix):
            matrix[i] = float(matrix[i])
        arr = np.array(matrix)

f_norm = np.linalg.norm(arr, 'fro')
print(f_norm)


