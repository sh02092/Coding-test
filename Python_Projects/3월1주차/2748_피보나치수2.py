a = []
a.append(0)
a.append(1)

for i in range(2, int(input()) + 1):
    a.append(a[i-2]+a[i-1])

print(a[-1])