import sys
input = sys.stdin.readline

word = list(map(str, input().split('-')))
temp = []
for i in range(len(word)):
    temp.append(word[i][0])
print(*temp, sep='')