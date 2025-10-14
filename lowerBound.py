def lower_bound(arr, target):
    L=len(arr)
    for i in range(L):
        if arr[i]>=target:
            return i
    return L


arr = [1, 2, 4, 4, 5]
f=lower_bound(arr, 4)
print(f)  
