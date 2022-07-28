# Solving

## 단지번호붙이기- BJ_2667
https://www.acmicpc.net/problem/2667
### 문제풀이
```python
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
home = list()
house = [[False for _ in range(n)] for _ in range(n)]
total_count = []

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    home.append(input().rstrip())

for i in range(n):
    for j in range(n):
        count = 0
        if home[j][i] == '1' and house[j][i] == False:
            count += 1
            house[j][i] = True
            dfs = deque([(j, i)])
            while dfs:
                y, x = dfs.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if home[ny][nx] == '1' and house[ny][nx] == False:
                            count += 1
                            dfs.append((ny, nx))
                            house[ny][nx] = True
        if count > 0:
            total_count.append(count)

total = sorted(total_count)
print(len(total))
if len(total) == 0:
    print(0)
else:
    for i in range(len(total)):
        print(total[i])

```
dfs 알고리즘을 통해 단지당 집 개수 구하여 총 단지 출력 후 단지당 집 개수를 오름차순으로 출력한다.
### 의견
단순한 dfs 알고리즘


## 타일 채우기- BJ_2133
https://www.acmicpc.net/problem/2133
### 문제풀이
```python
n = int(input())
tile = [0 for _ in range(16)]

tile[2//2] = 3
tile[4//2] = 11

if n % 2 == 0:
    if n > 4:
        for i in range(3, n//2 + 1):
            tile[i] = 3 * tile[i - 1] + 2 * sum(tile[:i - 1]) + 2
    print(tile)
    print(tile[n//2])
else:
    print(0)
```
홀수일 경우 존재하지 않는다.
짝수일 경우만 따지므로 n // 2 로 index 따지는 규칙 찾는 dp 문제
dp[n - 2] * 3 + (dp[n - 4] + dp[n - 6] + dp[n - 8] + ... + dp[2]) * 2 + 2(뒤집어진 갈고리 2개씩 추가하는 형태)
### 의견
2개씩 더해지는 추가 형태의 규칙을 찾기가 까다로웠다.