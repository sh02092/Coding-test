def solution(s):
    answer = -1
    len_s = 0
    s = list(s)
    while 1:
        len_s = len(s)
        if len(s) == 0:
            break
        else:
            i = 1
            while 1:
                if i > len(s):
                    break
                if s[i - 1] == s[i]:
                    del s[i - 1:i + 1]
                i += 1
                
        if len_s == len(s):
            break
            
    if len_s == 0:
        return 1
    else:
        return 0

print(solution('cdcd'))