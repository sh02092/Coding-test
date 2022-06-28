temp = [0] * 42
count = 0
for i in range(10):
    num = int(input())
    temp[num%42] += 1
for i in range(42):
    if temp[i]>0:
        count += 1
print(count)