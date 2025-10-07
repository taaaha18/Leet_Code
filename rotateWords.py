def rotate(starr):
    if not starr:
        return starr

    s_list = list(starr)
    n = len(s_list)
    first = 0

    for record in range(n + 1):  
        if record == n or s_list[record] == ' ':
           
            left, right = first, record - 1
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

            first = record + 1 

    return ''.join(s_list)



#######################*****OR*****#############################

def reverseWords(s):
   
    words = s.split(' ')
    
   
    reversed_words = [word[::-1] for word in words]
    
   
    return ' '.join(reversed_words)

s = "Let's take LeetCode contest"
print(reverseWords(s))
