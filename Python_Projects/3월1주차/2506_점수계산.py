num = int(input())
cor = list(map(int, input().split()))
total = 0
temp = 0
for i in range(len(cor)):
    if cor[i] == 1:   
        temp += 1
    elif cor[i] == 0:
        temp = 0
    total += temp
print(total)