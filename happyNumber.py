def isHappy(n):
    seen = set()  # to detect cycles

    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10
        n = total

    if n == 1:
        print("True")
    else:
            print("False")

isHappy(19)  
isHappy(2)  