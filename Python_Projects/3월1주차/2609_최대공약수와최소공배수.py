a = list(map(int, input().split()))
a.sort()


ans_1 = 1
ans_2 = 1
for i in range(1, a[1] + 1):
    if a[0] % i == a[1] % i == 0:
        ans_1 = i

print(ans_1)
print(a[0] * a[1] // ans_1)