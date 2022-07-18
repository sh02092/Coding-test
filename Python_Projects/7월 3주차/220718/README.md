# Solving

## 퇴사2- BJ_15486
https://www.acmicpc.net/problem/15486
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
t_ = list()
p_ = list()
dp = [0 for _ in range(n + 1)]
total = 0

for _ in range(n):
    t, p = map(int, input().split())
    t_.append(t)
    p_.append(p)

for i in range(n):
    total = max(total, dp[i])
    if i  + t_[i] <= n:
        dp[i + t_[i]] = max(total + p_[i], dp[i + t_[i]])

print(max(dp))
```
퇴사하는 날(n)까지 최대한 상담을 많이 하기 위해 n 이하의 날 까지 가능한 모든 상담을 하여 dp list에 넣어 max 값을 출력한다.

### 의견
이전에 풀어봤던 비슷한 유형의 dp문제였다. 하지만 풀어본지 시간이 좀 지났어서 기억하는데 시간이 좀 걸렸다.