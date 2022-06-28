import sys
input = sys.stdin.readline

n = int(input())
num = []
for i in range(n):
    num.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(num[i])):
        if j == 0:
            num[i][j] += num[i - 1][j]
        elif j == len(num[i]) - 1:
            num[i][j] += num[i - 1][j - 1]
        else:
            num[i][j] += max(num[i - 1][j], num[i - 1][j - 1])

# k = 2
# for i in range(1, n):
#     for j in range(k):
#         if j == 0:
#             num[i][j] += num[i - 1][j]
#         elif j == i:
#             num[i][j] += num[i - 1][j - 1]
#         else:
#             num[i][j] += max(num[i - 1][j], num[i - 1][j - 1])
#     k += 1

print(max(num[n - 1]))