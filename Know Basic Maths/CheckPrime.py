from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def prime(n):
    if n<=1:
        return 'NO'
    for i in range(2,n):
        if n%i==0:
            return 'NO'
    return 'YES'

n=int(input())
print(prime(n))
