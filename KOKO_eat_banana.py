def eat(piles, hour):
    def can_eat(speed):
        time=0
        for pile in piles:
            time+=(pile+speed-1)//speed
        return time<=hour
    low, high=1, max(piles)
    while low<=high:
        mid=(low+high)//2
        if can_eat(mid):
            high=mid-1
        else:
            low=low+1