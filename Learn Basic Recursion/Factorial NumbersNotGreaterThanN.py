from typing import *

def fact(n:int)->None:
    if n==0:
        return 1 
    else:
        return n*fact(n-1)
    

def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    ar=[]
    for i in range(1,n+1):
        t=fact(i)
        if t<=n:
            ar.append(t)
        else:
            break
    return ar
