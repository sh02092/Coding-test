import sys
input = sys.stdin.readline

num = int(input())
pay = [0] + list(map(int, input().split()))
# i개 구매할 떄 최대 값
dp = [0 for _ in range(num + 1)]

for i in range(1, num + 1):
    for k in range(1, i + 1):
        dp[i] = max(dp[i], dp[i-k] + pay[k])
print(dp[-1])

