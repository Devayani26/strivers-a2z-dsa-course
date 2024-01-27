def mergeSort(arr: [int], l: int, r: int):
    if l<r:
        mid=(l+r)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    i=l
    j=mid+1
    k=0
    temp=[]
    
    while i<=mid and j<=r:
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i=i+1 
        else:
            temp.append(arr[j])
            j=j+1

    while i<=mid:
        temp.append(arr[i])
        i +=1
    while j<=r:
        temp.append(arr[j])
        j +=1
    
    for i in range(len(temp)):
        arr[l+k]=temp[i]
        k =k+1
