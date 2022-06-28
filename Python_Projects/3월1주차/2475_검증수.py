temp = list(map(int, input().split()))
total = 0
for i in range(len(temp)):
    total += pow(temp[i], 2)
print(total % 10)