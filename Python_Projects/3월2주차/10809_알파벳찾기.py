word = input()
temp = [-1] * 26 # 97
for i in range(len(word)):
    if temp[ord(word[i]) - 97] == -1:
        temp[ord(word[i]) - 97] = i

print(*temp)