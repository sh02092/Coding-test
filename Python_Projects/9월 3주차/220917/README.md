# Solving

## 로또
https://www.acmicpc.net/problem/6603
### 문제풀이
```python
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

while 1:
    k_s = deque(deque(map(int, input().split())))
    if k_s[0] == 0:
        break

    k = k_s[0]
    k_s.popleft()
    sCombK = list(combinations(k_s, 6))
    for i in sCombK:
        print(*i)
    print()
```
순열을 import 하여 가능한 모든 경우의 수 출력한다.
### 의견
순열을 사용한 간단한 문제였다. 모든 경우의 수를 직접 출력해볼까 생각도 했지만 다음에 비슷한 문제가 나오면 해보는걸로..


## 주사위 굴리기
https://www.acmicpc.net/problem/14499
### 문제풀이
```python
import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

# x: row, y: col
# 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0 for _ in range(6)]

moves = list(list(map(int, input().split())))
for move in moves:
    # 지도를 벗어나면 바로 다음 move로
    if x + dx[move] < 0 or x + dx[move] > n-1 or y + dy[move] < 0 or y + dy[move] > m-1:
        continue

    nx = x + dx[move]
    ny = y + dy[move]

    # 주사위 Index 값 변경을 위한
    # swap용 변수
    diceIdx_0 = dice[0]
    diceIdx_1 = dice[1]
    diceIdx_2 = dice[2]
    diceIdx_3 = dice[3]
    diceIdx_4 = dice[4]
    diceIdx_5 = dice[5]
    
    # 주사위 Index 값 변경
    if   move==1: # 동
        dice[0]=diceIdx_2
        dice[1]=diceIdx_0
        dice[2]=diceIdx_5
        dice[5]=diceIdx_1
    elif move==2: # 서
        dice[0]=diceIdx_1
        dice[1]=diceIdx_5
        dice[2]=diceIdx_0
        dice[5]=diceIdx_2
    elif move==3: # 북
        dice[0]=diceIdx_4
        dice[3]=diceIdx_0
        dice[4]=diceIdx_5
        dice[5]=diceIdx_3
    elif move==4: # 남
        dice[0]=diceIdx_3
        dice[3]=diceIdx_5
        dice[4]=diceIdx_0
        dice[5]=diceIdx_4
    
    # 지도 칸의 조건
    if graph[nx][ny]==0:
        graph[nx][ny]=dice[0]
    else:
        dice[0]=graph[nx][ny]
        graph[nx][ny]=0
    
    print(dice[5])
    x, y = nx, ny
```
주사위가 동, 서, 북, 남으로 이동할 때 주사위의 각 Index 값이 어떻게 바뀌는지 파악하여 dice list에 [아랫값, 동, 서, 북, 남, 윗값] 으로 초기화 시켜 지도 칸의 조건에 따라 지도 값을 변경하고, dice[5]인 윗값을 출력한다.
### 의견
주사위 문제라서 너무 헷갈렸다. 처음에 모든 경우를 구현하면 될 것 같아 구현했지만, 주사위 방향이 돌아갈 상황을 고려하지 않았고, 주사위를 직접 만져보며 동, 서, 북, 남으로 이동할 때 Index 값이 바뀌는지 파악해 하드코딩하여 해결할 수 있었다. 찝찝한 결말..