# Solving

## 회의실 배정 2
https://www.acmicpc.net/problem/19621
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
time = [0]  # 회의 진행 시간
total = [0]     # 최대 인원
for _ in range(n):
    a, b, t = map(int, input().split())
    time.append(t)
time.append(0)

# i 번째 회의를 진행할 경우 
# (i - 1)번째 최댓값이었던 회의 시간과 비교하여 
# 큰 경우를 i번째 회의 시간의 최댓값으로 
total.append(time[1])
for i in range(2, n + 1):   
    total.append(max(total[i - 2] + time[i], total[i - 1]))

print(total[-1])
```
점화식을 세워 회의 진행 가능한 최대 인원을 구한다.
### 의견
많이 접했던 문제였지만, 매번 점화식을 생각하지 못해 구글의 힘을 빌렸던 문제였다. 하지만 이번 기회에 끝까지 생각해보며 풀어보고 싶은 마음에 계속 고민과 고민을 반복한 끝에 점화식을 생각해낼 수 있었고, 다음에 이런 문제가 나온다면 더욱 빠른 시간 안에 해결할 수 있을 것 같다.


## 한 줄로 서기
https://www.acmicpc.net/problem/1138
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
graph = list(False for _ in range(n))
ansLi = list(0 for _ in range(n))
cnt = 0

for j in range(len(li)):
    for i in range(len(li)):
        if graph[i] == True:    # 이미 존재하는 경우 넘기기
            continue
        else:   # 존재하지 않는 경우
            if cnt == li[j]:    # 왼쪽에 존재하는 사람 수를 세었을 때 입력한 값과 같은 경우
                graph[i] = True
                ansLi[i] = j + 1
                cnt = 0
                break
            else:       # 왼쪽에 존재하는 사람 수를 세었을 때 입력한 값과 다를 경우
                cnt += 1
print(*ansLi)
```
키가 가장 작은 1부터 N까지 차례로 입력 조건대로 왼쪽부터 키가 큰 사람이 몇명 존재하는지 count 하여 count 위치에 세운다. 
### 의견
가장 작은 사람부터 세우기 때문에 세운 이후인 True일 경우는 큰 사람 count를 세지 않고 False인 경우만 count하여 각 사람의 키 별 위치를 파악했다.


## 정사각형
https://www.acmicpc.net/problem/1485
### 문제풀이
```python
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ans = 0
    points = [[] for _ in range(4)]
    for i in range(4):
        points[i] = list(map(int, input().split()))
        
    points.sort(key = lambda x : x[1])
    points.sort(key = lambda x : x[0])

    diag1 = abs(points[-1][0] - points[0][0]) ** 2 + abs(points[-1][1] - points[0][1]) ** 2
    diag2 = abs(points[2][0] - points[1][0]) ** 2 + abs(points[1][1] - points[2][1]) ** 2
    len1 = abs(points[1][0] - points[0][0]) ** 2 + abs(points[1][1] - points[0][1]) ** 2
    len2 = abs(points[2][0] - points[0][0]) ** 2 + abs(points[2][1] - points[0][1]) ** 2

    # 두 변의 길이, 두 대각선의 길이가 같을 경우
    if diag1 == diag2 and diag1 > 0 and diag2 > 0 and len1 == len2 and len1 > 0 and len2 > 0:
        ans = 1
    print(ans)
```
한 점을 공유하는 두 변의 길이가 같고, 두 대각선의 길이가 같고, 모두 0보다 클 경우 정사각형으로 판별했다.
### 의견
정사각형으로 판별하는 기준을 그려보며 조건을 파악해 해결했다.


## 랭킹전 대기열
https://www.acmicpc.net/problem/20006
### 문제풀이
```python
import sys
input = sys.stdin.readline

p, m = map(int, input().split())
player = [[] for _ in range(p)]
graph = [False for _ in range(p)]
# 5명의 플레이어 들어갈 때 마다 게임 실행: Started!
# 전체 player 다 돌았는데 게임 실행 안될 경우: Waiting!
gameStk = []
for i in range(p):
    player[i] = list(map(str, input().split()))
    player[i][0] = int(player[i][0])

temp = False
for j in range(len(player)):
    if graph[j] == False:   # 방 만들기
        gameStk.append(player[j])
        graph[j] = True
        temp = True

        for i in range(j, len(player)):    # 만들어진 방에 플레이어 채우기
            if graph[i] == False and gameStk[0][0] - 10 <= player[i][0] <= gameStk[0][0] + 10:
                graph[i] = True
                gameStk.append(player[i])

            if len(gameStk) == m:   # 만들어진 방에 플레이어 모두 참
                break

    if temp:
        if len(gameStk) == m:   # 게임 시작
            print('Started!')
        else:                   # 게임 시작 못함
            print('Waiting!')
        
        gameStk.sort(key = lambda x : x[1])
        for i in range(len(gameStk)):
            print(*gameStk[i])
        gameStk = []
        temp = False
```
전체 플레이어를 돌면서 방에 들어가지 않은 플레이어에 대해 방을 만들어주고, 해당 플레이어부터 마지막 플레이어까지 전체적으로 돌며 조건을 만족시킬 경우 방에 플레이어를 넣었다. 전체 플레이어를 돌기 전에 방이 풀방이 될 경우 게임이 시작되고, 전체 플레이어를 돌때까지 풀방이 되지 않을 경우 게임이 시작하지 않도록 구성했다.
### 의견
문제에서 시키는대로 하면 되는 구현문제였다. 항상 구현문제를 풀면서 느끼지만 예외처리가 가장 중요한 것 같다. 테스트 케이스를 제외하고 생각해야 하는 조건이 꼭 있기 때문!


## 게임
https://www.acmicpc.net/problem/1072
### 문제풀이
```python
import sys
input = sys.stdin.readline

x, y = map(int, input().rsplit())
victory = y * 100 // x
ans = sys.maxsize   # 파이썬 최대 정수값: 9223372036854775807
l, r = 1, x

while l <= r:   # 이분탐색
    mid = (l + r) // 2

    curr_vic = (y + mid) * 100 // (x + mid)
   
    if curr_vic > victory:
        ans = min(mid,ans)
        r = mid - 1
    else:
        l = mid + 1

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
```
파이썬 최대 정수값(sys.maxsize)을 더해도 z가 바뀌지 않을 경우 -1 출력, 나머지 경우엔 해당 정수값을 출력한다. 이분탐색 알고리즘 사용.
### 의견
나름 많이 생각했다 생각했는데 10번 이상 실패가 뜨니 화가 났다... 구글링을 했더니 허무한 결과.. 이분탐색이라니... 신나게 구현문제를 풀다가 이분탐색과 같은 간단한 알고리즘 조차 기억이 안나서 풀지 못했다는 것이 화가나는 문제였다..