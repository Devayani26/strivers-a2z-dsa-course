from typing import List

 

def generateFibonacciNumbers(n: int) -> List[int]: 

    array=[]

    f1=0

    f2=1

    if(n<=1):

        array.append(f1)

    else:

        array.append(f1)

        array.append(f2)

    return fib(f1,f2,array,n)

    

 

def fib(f1,f2,array,n):

    f3=f1+f2

    if(len(array)==n):

        return array

    array.append(f3)

    return fib(f2,f3,array,n)
