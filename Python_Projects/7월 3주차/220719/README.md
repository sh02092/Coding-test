# Solving

## 테트로미노- BJ_14500
https://www.acmicpc.net/problem/14500
### 문제풀이
```python
dx = [-1,1,0,0]
dy = [0,0,1,-1]

result = 0

def dfs(s_x, s_y, cnt, sum):
    global result, max_val
    visited[s_x][s_y] = True

    # 남은 블럭이 모두 최댓값이라 해도 현재의 최대를 넘길수 없을때 조기종료 해버림
    if sum + max_val * (4-cnt) <= result:
        return

    # 사각형 4개가 된 순간 최댓값을 갱신한다.
    if cnt == 4:
        result = max(result, sum)
        return

    # 상하좌우 이동
    for i in range(4):
        # 이동가능하면
        d_x, d_y = s_x+dx[i], s_y+dy[i]
        if 0<=d_x<n and 0<= d_y <m and not visited[d_x][d_y]:
                dfs(d_x,d_y, cnt+1, sum+graph[d_x][d_y])
                visited[d_x][d_y] = False # 목적지를 풀어주는것임

def adjust(graph, s_x, s_y):
    global result
    adj = []
    for i in range(4):
        # 이동가능하면
        if s_x+dx[i] >=0 and s_x+dx[i]<n and s_y+dy[i] >=0 and s_y+dy[i] <m:
            adj.append(graph[s_x+dx[i]][s_y+dy[i]])

    if len(adj)>=3:
        temp = graph[s_x][s_y]+sum(sorted(adj, reverse=True)[:3])
        result = max(result, temp)


import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 

graph = []

visited = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

max_val = max(max(*graph))

for i in range(n):
    for j in range(m):
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False
        adjust(graph, i,j)

print(result)
```
dfs 알고리즘을 이용해 브루트 포스 사용. ㅗ 모양을 제외한 나머지 모양에 대해 count가 4가 되면 리턴.

### 의견
너무 어렵다. 아직 모르겠다..


## Puyo Puyo- BJ_11559
https://www.acmicpc.net/problem/11559
### 문제풀이
```python
from collections import deque
import sys
input = sys.stdin.readline

# 필드 채우기
field_letter = []
for i in range(12):
    field_letter.append(list(input()))

# 선택된 뿌요 판별을 위한 list
field = [[False for _ in range(6)] for _ in range(12)]
# 상하좌우로 연결된 뿌요 count
count = 0
# 지운 이후 남아있는 뿌요 count
letter_count = []
# 총 몇 연쇄가 되는지 count
full_count = 0
# 하나도 터지지 않을 경우 판별용 list
non = []


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# dfs
def dfs(start_y, start_x):
    # 시작점이 '.'일 경우 바로 다음 시작점으로
    if field_letter[start_y][start_x] == '.':
        return

    # count 되는 점 deque 에 넣어 지우기 위한 list
    dot_count = deque([(start_y, start_x)])
    # 시작점 스택에 넣기
    q = deque([(start_y, start_x)])
    # 뿌요 색에 따른 수 count
    q_value = {'R': 0, 'G': 0, 'B': 0, 'P': 0, 'Y': 0}
    # 시작점 뿌요 색 dictionary count +1
    q_value[field_letter[start_y][start_x]] += 1

    while q:
        y, x = q.popleft()
        # 시작점 밟음
        field[y][x] = True
        # 동 서 남 북 에 대해
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 조건 만족할 경우
            if nx >= 0 and nx < 6 and ny >= 0 and ny < 12:
                if field_letter[ny][nx] == field_letter[y][x] and field[ny][nx] == False:
                    # 스택에 추가
                    q.append((ny, nx))
                    # 상하좌우로 연결된 뿌요 deque 에 추가
                    dot_count.append((ny, nx))
                    # 뿌요 색 count +1
                    q_value[field_letter[ny][nx]] += 1
                    # 상하좌우로 연결된 뿌요 밟음
                    field[ny][nx] = True

    # 4개 이상 상하좌우로 연결될 경우
    count = q_value[field_letter[start_y][start_x]]
    if count >= 4:
        # count 된 뿌요 '.'으로 바꾸기
        for i in range(len(dot_count)):
            field_letter[dot_count[i][0]][dot_count[i][1]] = '.'
        return count


while 1:
    letter_count.append(0)

    # (11, 0) 부터 (0, 5) 까지 모두
    for y in reversed(range(12)):
        for x in range(6):
            count = dfs(y, x)
            non.append(count)
    # 밟은 뿌요들 초기화
    field = [[False for _ in range(6)] for _ in range(12)]

    # 중력의 영향을 받아 아래로 떨어지는 뿌요
    for i in range(6):
        letter = []
        for j in range(12):
            # 색깔 뿌요들 따로 저장
            if field_letter[j][i] != '.':
                letter.append(field_letter[j][i])
                # 뿌요들이 있던 자리 '.'으로
                field_letter[j][i] = '.'
        # 뿌요들 거꾸로 채워주기
        for j in range(len(letter)):
            field_letter[-(j + 1)][i] = letter[-(j + 1)]
        letter_count[-1] += len(letter)

    if len(letter_count) >= 2:
        # 하나도 터지지 않을 경우, while 문 종료
        if not non:
            print(0)
            break
        # letter_count 가 감소하지 않다면, while 문 종료
        elif letter_count[-1] == letter_count[-2]:
            print(full_count)
            break

    full_count += 1
```
전체 뿌요에 대해 dfs 알고리즘을 사용해 모든 좌표에 4개 이상 붙어있을 경우의 뿌요 색깔 그룹을 찾아 '.'으로 바꾼다. 없앤 뿌요 자리를 위의 다른 뿌요로 채우고, 연쇄가 총 몇 번 연속으로 일어나는지 full_count 로 구한다. 

### 의견
혼자 풀었을 때 정답이 41%에서 틀렸다고 떴는데 왜 틀렸는지 알고싶다.


## 베르트랑 공준
https://www.acmicpc.net/problem/4948
### 문제풀이
```python
# 에라토스테네스의 체
from math import sqrt
import sys
input = sys.stdin.readline

# 소수 list
num = []

# 시간 초과 나서 범위 내의 n에 대해 소수를 판별하고 실행한다.
for i in range(2, 123456 * 2 + 1):
    count = 0
    # 소수와 약수의 성질
    # 소수의 성질: 1과 자기 자신을 제외한 약수를 갖지 않는다.
    # 약수를 갖는 수의 성질: 1부터 자기 자신의 제곱근 사이에 약수의 절반을 갖는다.
    # -> 2n의 제곱근보다 작거나 같은 수까지 에라토스테네스의 체를 이용해 소수 판별
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            count += 1
            break

    if count == 0:
        num.append(i)

while 1:
    n = int(input())
    sosu = 0
    if n == 0:
        break
    for i in num:
        if n < i <= 2*n:
            sosu += 1
    print(sosu)
```
전체 n에 대한 범위에서 에라토스테네스의 체를 이용해 소수를 모두 구한다.

### 의견
전체 n에 대한 범위에서 구할 생각을 하지 못하여 계속 시간초과를 경험했다.