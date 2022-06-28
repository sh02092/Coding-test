a = []
a.append(0)
a.append(1)
n = int(input())
for i in range(1, n):
    a.append(a[i - 1] + a[i])
if n == 0:
    print(0)
else:
    print(a[-1])