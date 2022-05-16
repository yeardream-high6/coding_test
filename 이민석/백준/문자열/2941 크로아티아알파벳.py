import sys
sys.stdin=open("input.txt", "rt")


alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in alphabet :
    a = a.replace(i, '0')
print(len(a))