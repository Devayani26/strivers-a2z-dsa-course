from typing import List

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    n=len(arr)
    for i in range(0,n):
        min_val=i 
        for j in range(i+1,n):
            if arr[j]<arr[min_val]:
                min_val=j 
        arr[i],arr[min_val]=arr[min_val],arr[i]
    return arr
