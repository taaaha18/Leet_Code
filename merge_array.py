def merge(arr1, arr2):
    if not arr1:
        return arr2
    elif not arr2: 
        return arr1
    elif not arr1 and not arr2:
        return []

    for i in range(len(arr1)):
       if arr1[i]>arr2[i]:
              arr1.append(arr1[i])
              arr1[i]=arr2[i]

    arr1.sort()          
