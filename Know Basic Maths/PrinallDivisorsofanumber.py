from typing import List

def printDivisors(n: int) -> List[int]:
    div=[]
    for i in range(1,n+1):
        if n%i==0:
            div.append(i)
    return div