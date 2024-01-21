from os import *
from sys import *
from collections import *
from math import *

def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        digit_int = int(digit)
        digit_power = digit_int ** num_len
        sum += digit_power
    if sum==n:
        print('true')
    else:
        print('false')
n=int(input())
is_armstrong(n)
