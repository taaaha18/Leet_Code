def bukket(garden, num, bukket_size):
    n = len(garden)
    if num * bukket_size > n:
        return -1

    low, high = min(garden), max(garden)
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        flowers = 0
        bouquets = 0

        # Count how many bouquets can be formed by 'mid' days
        for day in garden:
            if day <= mid:
                flowers += 1
                if flowers == bukket_size:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0  # reset if a flower hasn't bloomed yet

        if bouquets >= num:
            answer = mid      # store this mid as a valid day
            high = mid - 1    # try to find a smaller possible day
        else:
            low = mid + 1

    return answer
