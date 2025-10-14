def books(pages, users):
    low = max(pages)
    high=sum(pages)
   
    while(low<high):
        mid =(low+high)//2
        required_users=1
        current_sum=0
       
        for p in pages:
            if current_sum+p>mid:
                required_users+=1
                current_sum=0
            current_sum+=p
        if required_users>users:
            low=mid+1
        else:
            high=mid    

    return low   