total = 0
num = []
for i in range(10):
    a, b = map(int, input().split())
    total -= a
    num.append(total)
    total += b
    num.append(total)
num.sort()
print(num[-1])