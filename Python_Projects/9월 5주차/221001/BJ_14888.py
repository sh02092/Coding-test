# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기- BJ_14888
s = '3people    UnFo3lowed me'
s = s.capitalize()
print(s)
# 홍보자료로 발탁
# ITRC 잘 풀어서 말하기

def solution(s):
    answer = ''
    temp = s.split(' ')
    for i in range(len(temp)):
        if temp[i]:
            if 97 <= ord(temp[i][0]) <= 122:
                temp[i] = temp[i][0].upper() + temp[i][1:].lower()
            else:
                temp[i] = temp[i][0] + temp[i][1:].lower()
    # print(temp)
    answer = ' '.join(temp)
    # 65 ~ 90, 97 ~ 122
    
    
    return answer

print(solution(s))