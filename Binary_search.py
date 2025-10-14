def binary_search(self,arr, target):
    l=arr.length()
    low=0
    high=l-1
    while (low<=high):
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
            
    return -1       