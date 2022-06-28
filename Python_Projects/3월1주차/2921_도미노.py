num = int(input())
total = 0
for i in range(1, num + 1):
    total += (i * (i + 1))
    for j in range(1, i + 1):
        total += j

print(total)