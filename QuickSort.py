"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    if startIndex < endIndex:
        pivotIndex = partition(arr, startIndex, endIndex)
        quickSort(arr, startIndex, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, endIndex)

def partition(arr: List[int], startIndex: int, endIndex: int):
    pivot = arr[endIndex]
    i = startIndex - 1
    for j in range(startIndex, endIndex):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[endIndex] = arr[endIndex], arr[i + 1]
    return i + 1
