import numpy as np
import sys
import csv

file_name = sys.argv[1]

with open(file_name + ".csv") as file:
    csvreader = csv.reader(file, delimiter = "\t")
    

    for matrix in csvreader:
        m = [list(0 for i in range(matrix)) for j in range(matrix)]
        for i in range(matrix):
            for j in range(matrix):
                m[i][j] = float(matrix[i][j])
        arr = np.array(m)

f_norm = np.linalg.norm(arr, 'fro')
print(f_norm)


