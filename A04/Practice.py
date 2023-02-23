"""This file is used for problem 1 of assignment 4. 
This file can be ignored because all the answers are on the word doc submitted through canvas"""
import task5
a = ['Manann', 'Bhargava', 'UW Madison', 'ME459', 'Mechnical Engineering']
b=a #both variables a and b are pointing to the same list in the memory 
b[1] = 'Not Manann' #changes made to b can be seen in a due to the reason above
print(a)
print(b)
c=a[:] #deep copy of list a, they do not point to the same list
c[2] = 'MIT'#any changes made now to c will not be shown in a
print(c)
print(a)



