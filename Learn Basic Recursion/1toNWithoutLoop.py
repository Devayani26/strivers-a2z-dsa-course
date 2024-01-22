from typing import List

def printNos(x: int) -> List[int]: 
    # Write your code here
    lst=[]
    for i in range(1,x+1):
        lst.append(i)
    return lst
