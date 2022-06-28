total = 0
temp = [0] * 100
for _ in range(10):
    num = int(input())
    total += num
    temp[num // 10] += 1

print(total//10)
print(temp.index(max(temp))*10)