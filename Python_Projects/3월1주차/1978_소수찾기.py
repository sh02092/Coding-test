num = int(input())
total = 0
temp = list(map(int, input().split()))
for i in range(num):
    if temp[i] > 1:
        for j in range(2, temp[i] + 1):
            if temp[i] % j == 0:
                if j == temp[i]:
                    total += 1
                break

print(total)