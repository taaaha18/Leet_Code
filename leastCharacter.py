def function(arr):
    if not arr:
        return None
    left=0
    count={a:0,b:0,c:0}
    substring=0

    for right in range (len(arr)):
        count[arr[right]]+=1

        while all(count[a]>0 for a in "abc"):
            substring+=len(arr)-right
            count[arr[left]]-=1
            left+=1