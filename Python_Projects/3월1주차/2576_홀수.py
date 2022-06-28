temp = []
total = 0
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        total += num
        temp.append(num)

if len(temp) == 0:
    print(-1)
else:
    temp.sort()
    print(total)
    print(temp[0])