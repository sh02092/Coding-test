# Solving

## 빗물
https://www.acmicpc.net/problem/14719
### 문제풀이
```python
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
temp = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):   # i 기준 
    leftMax = max(temp[:i])        # 왼쪽으로 가장 높은
    rightMax = max(temp[i+1:])     # 오른쪽으로 가장 높은

    comp = min(leftMax, rightMax)    # 왼쪽, 오른쪽 중 더 낮은

    if temp[i] < comp:      # i번째보다 낮으면 빗물 존재
        ans += comp - temp[i]

print(ans)
```
i번째 칸에서 빗물이 존재할 조건으로 유무를 판단해 값을 계산한다.
### 의견
i번째 칸별로 나눠 존재할지를 따지면 쉽게 풀리는데 칸별로 나눌 생각을 하는데 오래걸렸다.

## 떡 먹는 호랑이
https://www.acmicpc.net/problem/2502
### 문제풀이
```python
import sys
input = sys.stdin.readline

d, k = map(int, input().split())

temp = [0 for _ in range(d)]
temp[0] = 'x'
temp[1] = 'y'
for i in range(2, d):
    temp[i] = temp[i - 2] + temp[i - 1]

firNum = temp[-1].count('x')    # 첫째날 count
secNum = temp[-1].count('y')    # 둘째날 count

a = 1   # 첫째날 개수
b = 0   # 둘째날 개수
while 1:
    if (k - firNum * a) % secNum == 0:  # 1차 방정식 풀기
        b = (k - firNum * a) // secNum
        break
    a += 1

print(a)
print(b)
```
첫째날 떡 count와 둘째날 떡 count를 구해 1차 방정식을 풀어 해결한다.
### 의견
1차 방정식을 구해 수를 대입해보며 방정식에 맞는 해를 구하는 문제


## 꽃길
https://www.acmicpc.net/problem/14620
### 문제풀이
```python
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))
# 동 서 남 북 으로 체크
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 가능한 모든 좌표 경우의수
dot = list(combinations([(x, y) for x in range(1, n - 1) for y in range(1, n - 1)], 3))
ans = []

for i in range(len(dot)):
    flower = [[False for _ in range(n)] for _ in range(n)]  # 꽃이 있는 자리: True
    subAns = 0
    temp = False
    for x, y in dot[i]:
        if flower[x][y] == False:   # 꽃 씨앗 없을 경우
            flower[x][y] = True
            subAns += graph[x][y]
            for dx, dy in dxdy:     
                if flower[x + dx][y + dy] == False:     # 꽃잎 없을 경우
                    flower[x + dx][y + dy] = True
                    subAns += graph[x + dx][y + dy]
                else:                                   # 꽃잎 이미 있을 경우
                    temp = True
        else:                       # 꽃 씨앗 이미 있는 경우
            temp = True
        if temp:
            break
    if not temp:        # 꽃이 지지 않고 모두 필 경우
        ans.append(subAns)

if ans:
    print(min(ans))
else:
    print(0)
```
브루트포스 알고리즘 사용해 꽃이 필 수 있는 모든 경우의 수를 구해 최소 비용 구한다.
### 의견
코테는 파이썬