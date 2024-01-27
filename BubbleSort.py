from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
