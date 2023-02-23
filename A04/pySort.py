"""
PROBLEM 4
This file contains the code for a bubble sort. 
"""
def sorter(A):
    C=A[:]#deep copy of A so A doesn't change 
    n = len(A) #number of elements in list A
    for j in range(n-1):
        for i in range(n-j-1):
            if(C[i]>C[i+1]):
                temp = C[i] #switiching 2 values in the list requries a temporary value
                C[i] = C[i+1] 
                C[i+1]=temp
          
    return C

#This part of the code below was used to test whether the code works the way it is suppose to, please ignore
# A = [12, 45, 23, 51, 19, 8]
# print(A)
# C = sorter(A)
# print(sorter(A))