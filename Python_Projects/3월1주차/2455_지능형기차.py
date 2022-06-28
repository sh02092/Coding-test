arr = []
total = 0
for i in range(4):
    a, b = map(int, input().split())
    total -= a
    arr.append(total)
    total += b
    arr.append(total)
print(max(arr))