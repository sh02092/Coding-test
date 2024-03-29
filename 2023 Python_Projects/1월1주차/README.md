# Solving

## NBA 농구
https://www.acmicpc.net/problem/2852
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
time_1, time_2 = [0,0], [0,0]
temp = True
cnt_win = 0 # 양수: 1 이길때, 음수: 2 이길때
pres_time = list() # 현재 시간

for _ in range(n):
    win, time = map(str, input().split())
    win = int(win)
    time = list(map(int, time.split(':')))
    if win == 1:
        cnt_win += 1
    elif win == 2:
        cnt_win -= 1
    
    if cnt_win == 1 and win == 1:   # 1이 이기고 있을 경우
        temp = True
        pres_time = time
    elif cnt_win == -1 and win == 2:    # 2가 이기고 있을 경우
        temp = False
        pres_time = time
    elif cnt_win == 0:  # 비기게 될 경우: 이기고 있던 player 시간 계산
        if temp:    # 1이 이겼던 시간 계산
            if time[1] >= pres_time[1]:
                time_1[1] += time[1] - pres_time[1]
            else:
                time_1[1] += time[1] + 60 - pres_time[1]
                time[0] -= 1
            time_1[0] += time[0] - pres_time[0]
            if time_1[1] > 59:
                time_1[0] += time_1[1] % 60
                time_1[1] %= 60

        else:   # 2가 이겼던 시간 계산
            if time[1] >= pres_time[1]:
                time_2[1] = time[1] - pres_time[1]
            else:
                time_2[1] += time[1] + 60 - pres_time[1]
                time[0] -= 1
            time_2[0] += time[0] - pres_time[0]
            if time_2[1] > 59:
                time_2[0] += time_2[1] % 60
                time_2[1] %= 60

if cnt_win != 0:    # 마지막에 무승부 아닐 경우
    time = [48, 0]
    if temp:
        if time[1] >= pres_time[1]:
            time_1[1] += time[1] - pres_time[1]
        else:
            time_1[1] += time[1] + 60 - pres_time[1]
            time[0] -= 1
        time_1[0] += time[0] - pres_time[0]
        if time_1[1] > 59:
            time_1[0] += time_1[1] % 60
            time_1[1] %= 60
    else:
        if time[1] >= pres_time[1]:
            time_2[1] = time[1] - pres_time[1]
        else:
            time_2[1] += time[1] + 60 - pres_time[1]
            time[0] -= 1
        time_2[0] += time[0] - pres_time[0]
        if time_2[1] > 59:
            time_2[0] += time_2[1] % 60
            time_2[1] %= 60

print('{:0>2}:{:0>2}'.format(time_1[0], time_1[1]))
print('{:0>2}:{:0>2}'.format(time_2[0], time_2[1]))
```
특정 플레이어가 이길 때부터 무승부가 되기 전까지의 시간을 측정한다.
### 의견
아무리 봐도.. 틀린 부분을 찾을 수가 없는데 6%에서 실패가 뜬다. 반례 케이스를 찾고 싶다...


## 동전 0
https://www.acmicpc.net/problem/11047
### 문제풀이
```python
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
aList = [0 for _ in range(n)]
cnt = 0
for i in reversed(range(n)):
    aList[i] = int(input())

for i in aList:
    if k < i:
        continue
    else:
        cnt += k // i
        k %= i

print(cnt)
```
그리디 알고리즘
### 의견
그리디 알고리즘


## 곱셈
https://www.acmicpc.net/problem/1629
### 문제풀이
```python
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def multi (a,n):
  if n == 1:
      return a%c
  else:
      tmp = multi(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp *a) %c
          
print(multi(a,b))
```
나머지 분배 법칙: (a x b) % c = (a % c) x (b % c) % c 적용한다.
### 의견
나머지 분배 법칙을 모르면 풀기 힘든 문제.. 나머지 분배 법칙을 처음 봤다.

## 파도반 수열
https://www.acmicpc.net/problem/9461
### 문제풀이
```python
import sys
input = sys.stdin.readline

nCase = [0 for _ in range(101)]
nCase[1] = 1
nCase[2] = 1
nCase[3] = 1
nCase[4] = 2
nCase[5] = 2
for i in range(6, len(nCase)):
    nCase[i] = nCase[i - 1] + nCase[i - 5]

t = int(input())
for _ in range(t):
    print(nCase[int(input())])
```
6번째 수부터 규칙을 찾아 규칙에 맞게 100번째 까지 수를 구한다.
### 의견
간단한 규칙을 찾으면 풀 수 있는 DP 문제.

## 유기농 배추
https://www.acmicpc.net/problem/1012
```python
import sys
input = sys.stdin.readline

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and s[q][w] == 1:
                s[q][w] = 0
                queue.append([q, w])

for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
    for q in range(n):
        for w in range(m):
            if s[q][w] == 1:
                bfs(q, w)
                s[q][w] = 0
                cnt += 1
    print(cnt)
```
bfs
### 의견
bfs 알고리즘


## 경로 찾기
https://www.acmicpc.net/problem/11403
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
#플로이드-워셜 알고리즘
for k in range(n): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(n):
        for j in range(n): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])
```
플로이드-워셜 알고리즘을 사용한다.
### 의견
처음 시도에는 입력 행렬에서 각 간선을 n번까지 타는 재귀함수를 사용하여 각 정점에서 다른 정점으로 가는 경로를 모두 탐색했다. 하지만 시간 초과가 발생하여 다른 알고리즘을 생각하다 플로이드-워셜 알고리즘을 발견하여 해당 알고리즘을 사용해 해결했다.


## 수리공 항승
https://www.acmicpc.net/problem/1449
### 문제풀이
```python
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [False for _ in range(1001)]
cnt = 1

water = list(map(int, input().split()))
water.sort()

for i in water:
    graph[i] = True

end = water[0] + l - 1
for i in range(1, len(water)):
    if water[i] > end:
        end = water[i] + l - 1
        cnt += 1
print(cnt)
```
테이프를 사용한 end 지점을 기준으로 물이 새는 곳보다 end가 더 0과 가깝다면 테이프를 하나 더 사용했다.
### 의견
물이 새는 곳이 한 칸이어서 문제에서 말하는대로 코드를 구성하여 해결했다.


## 카드2
https://www.acmicpc.net/problem/2164
### 문제풀이
```python
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
card = deque((i + 1) for i in range(n))

while len(card) > 1:
    card.popleft()
    x = card.popleft()
    card.append(x)

print(*card)
```
card 이름의 큐를 만들어 맨 앞 수를 버리고 그 다음 수를 맨 뒤에 넣는 과정을 큐의 크기가 1이 될 때까지 반복한다.
### 의견
큐를 사용하여 해결했다.


## 스위치 켜고 끄기
https://www.acmicpc.net/problem/1244
### 문제풀이
```python
import sys
input = sys.stdin.readline
n = int(input())    # 100 이하 자연수
switch = list(map(int, input().split()))    # n개 스위치 상태
nStu = int(input())     # 학생 수
for i in range(nStu):
    s, num = map(int, input().split())    # 성별, 받은 수
    num -= 1
    if s == 1:  # 남학생일 경우
        for j in range(num, n, num + 1):
            if switch[j] == 1:
                switch[j] = 0
            elif switch[j] == 0:
                switch[j] = 1
    elif s == 2:    # 여학생일 경우
        temp = 0
        while (0 <= num - temp and num + temp < n):
            if switch[num - temp] == switch[num + temp]:
                if switch[num - temp] == 1:
                    switch[num - temp] = 0
                    switch[num + temp] = 0
                elif switch[num - temp] == 0:
                    switch[num - temp] = 1
                    switch[num + temp] = 1
            else:
                break
            temp += 1
if len(switch) <= 20:   # 스위치 길이 21보다 작을 때
    print(*switch)
else:   # 스위치 길이 20보다 클 때
    for i in range(len(switch)):
        print(switch[i], end=' ')
        if (i + 1) % 20 == 0:
            print()
```
남학생일 경우 for문에서 선택한 자연수 크기만큼 더해가며 상태를 변경했고, 여학생일 경우 while문 조건에 맞을 때 temp 값을 더하고 뺀 값의 상태가 같을 경우 상태를 변경하고 temp 값을 1씩 키웠다. 
마지막으로 출력할 때 20보다 스위치 개수가 많을 경우 20개씩 끊어서 출력할 수 있도록 구성했다.
### 의견
구현 문제, 자연수 n 값, num 값을 다룰 때 주의가 필요함.