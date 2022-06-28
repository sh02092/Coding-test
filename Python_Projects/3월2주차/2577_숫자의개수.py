total = 1
for _ in range(3):
    num = int(input())
    total *= num

temp = [0] * 10
for i in range(len(str(total))):
    a = total % 10
    total //= 10
    temp[a] += 1

for i in range(10):
    print(temp[i])