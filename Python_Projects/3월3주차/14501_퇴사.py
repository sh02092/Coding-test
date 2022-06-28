
n = int(input())
t_i = []
p_i = []
for i in range(n):
    t, p = map(int, input().split())
    t_i.append(t)
    p_i.append(p)
temp = [0 for _ in range(n + 1)]

# n, n-1, n-2, n-3 ...
for i in range(n-1, -1, -1):
    if t_i[i] + i > n:
        temp[i] = temp[i + 1]
    else:
        temp[i] = max(p_i[i] + temp[i + t_i[i]], temp[i + 1])

print(temp[0])