# Solving

## 동전 1
https://www.acmicpc.net/problem/2293
### 문제풀이
```python
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)] # 코인의 종류
dp = [0 for _ in range(k + 1)]
dp[0] = 1 # index 0은 동전을 1개만 쓸 때 경우의 수를 고려

for i in coin:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])
```
특정 동전을 썼을 때 가치의 합이 i(1 <= i <= k)원이 되는 경우의 수
### 의견
난 멍청이... DP 너무 어렵다... 도저히 생각이 나질 않는다... 