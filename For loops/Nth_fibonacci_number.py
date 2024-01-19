from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def F(n):
    f=[0]*(n+1)
    f[0]=0
    f[1]=1
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]

n=int(input())
print(F(n))
