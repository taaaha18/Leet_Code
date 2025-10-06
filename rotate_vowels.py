def rotate_vowels(s):
    vowels = []
    s_list = list(s)  

   
    for i in range(len(s) - 1, -1, -1):
        if s[i] in 'aeiouAEIOU':
            vowels.append(s[i])

   
    for i in range(len(s_list)):
        if s_list[i] in 'aeiouAEIOU':
            s_list[i] = vowels.pop(0) 

    return ''.join(s_list) 



print(rotate_vowels("IceCreAm"))   
