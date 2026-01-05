import sys

a = 10 
b = 10

a = b

print(sys.getrefcount(a))
