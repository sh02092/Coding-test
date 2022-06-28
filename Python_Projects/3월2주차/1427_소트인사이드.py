num = int(input())
temp = []
while num >= 10:
    temp.append(num % 10)
    num //= 10
temp.append(num)

temp_sort = sorted(temp)
total = 0
count = 1
for i in range(len(temp_sort)):
    total += count * temp_sort[i]
    count *= 10

print(total)