from math import *

s = 0
for n in range(1, 51):
    s += ((n**n + 1) / (2*n**n + 1)) * sin(2*n**2 + 1)

print(s)
