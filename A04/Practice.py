a = ['Manann', 'Bhargava', 'UW Madison', 'ME459', 'Mechnical Engineering']
b=a
b[1] = 'Not Manann'
print(a)
print(b)
c=a[:]
c[2] = 'MIT'
print(c)
print(a)


