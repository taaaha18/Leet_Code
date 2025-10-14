def Nth_root(num,x):
    low=0
    high=num

    while(low<=high):
        mid=(low+high)//2
        print(mid)
        count=x+1
        pow=1
        while(count>1):
            pow=pow*mid
            count-=1
        if pow==num:
            return mid
        elif pow<num:
            low=mid+1
        else:
            high=mid-1
    return -1      

N=Nth_root(27,3)
print("the root is ", N)