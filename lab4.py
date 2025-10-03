from math import *

for n in range(1, 51):
    s = 0
    s += ((n**n + 1) / (2*n**n + 1)) * sin(2*n**2 + 1)

print(s)