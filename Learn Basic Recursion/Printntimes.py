from  typing import *

def printNtimes(n: int) -> List[str]:
    x="Coding Ninjas"
    if n>0:
        print(x,end=" ")
        printNtimes(n-1)
