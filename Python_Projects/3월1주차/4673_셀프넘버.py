# 1로 초기화한 크기 10000의 list
temp = [1 for i in range(9999)]

for i in range(1, len(temp) + 1):
    total = i
    while i >= 10:
        total += (i % 10)
        i //= 10
    total += (i % 10)
    if total < 10000:
        temp[total - 1] = 0

for i in range(len(temp)):
    if temp[i] == 1:
        print(i + 1)    

