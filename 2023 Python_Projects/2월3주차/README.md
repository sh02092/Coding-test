# Solving

## NBA 농구
https://www.acmicpc.net/problem/2852
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
win = [0, 0]
winT = [0, 0]
startT = 0
endT = 48 * 60
temp = -1

for i in range(n):
    teamNum, goalTime = map(str, input().split())
    num = int(teamNum) - 1
    m, s = goalTime.split(':')
    time = int(m) * 60 + int(s)
    win[num] += 1
    
    if win[0] > win[1] and win[0] == 1:     # 1번팀 이길때
        startT = time
        temp = 0
    elif win[0] < win[1] and win[1] == 1:   # 2번팀 이길때
        startT = time
        temp = 1
    elif win[0] == win[1]:  # 비길때
        endT = time
        winT[temp] += endT - startT

        # 초기화
        endT = 48 * 60
        win[0] = 0
        win[1] = 0

if endT == 48 * 60 and win[0] != win[1]:    # 어느 팀이든 이기고 있을때
    winT[temp] += endT - startT

ans1M = str(winT[0] // 60)
ans1S = str(winT[0] % 60)
ans2M = str(winT[1] // 60)
ans2S = str(winT[1] % 60)

if int(ans1M) < 10:
    ans1M = '0' + ans1M
if int(ans1S) < 10:
    ans1S = '0' + ans1S
if int(ans2M) < 10:
    ans2M = '0' + ans2M
if int(ans2S) < 10:
    ans2S = '0' + ans2S

print(ans1M + ':' + ans1S)
print(ans2M + ':' + ans2S)
```
1번팀이 이기고 있을때와 2번팀이 이기고 있을때의 경우를 잘 나눠 생각해서 푸는 구현문제
### 의견
반례를 생각하는게 제법 까다로웠던 구현문제였다. 좋은 문제!


## 상어 초등학교
https://www.acmicpc.net/problem/21608
### 문제풀이
```python
# https://www.acmicpc.net/problem/21608
# 상어 초등학교- BJ_21608

import sys

input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
graphLike = [[[] for _ in range(n)] for _ in range(n)]

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n ** 2):
    stu, li1, li2, li3, li4 = map(int, input().split())
    stuLike = [li1, li2, li3, li4]

    maxLike = 0     # max 좋아하는 학생수
    subGraph = [[0 for _ in range(n)] for _ in range(n)]       # 인접한 칸에 좋아하는 학생 수
    graphNextCond = [[False for _ in range(n)] for _ in range(n)]   # True끼리 다음 조건 비교
    for y in range(n):
        for x in range(n):
            cntLike = 0
            if graph[y][x] == 0:    # 한칸에는 한명씩!
                for j in range(4):  # 인접한 4칸에 좋아하는 학생 있는지 판별
                    if 0<=y+dy[j]<n and 0<=x+dx[j]<n:   # 범위 벗어나지 않도록
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if graph[ny][nx] in stuLike:    # 좋아하는 학생칸일 경우, cntLike += 1
                            cntLike += 1
                if maxLike < cntLike:   # 좋아하는 학생 max 값 바뀜
                    maxLike = cntLike
                subGraph[y][x] = cntLike
    # print('subGraph: ',subGraph)
    # print('maxLike: ', maxLike)
    cnt1 = 0
    x1, y1 = -1, -1
    for y in range(n):      ## 1번 조건
        for x in range(n):
            if subGraph[y][x] == maxLike and graph[y][x] == 0:   # 1번조건 만족할 경우, True
                cnt1 += 1   # 1번 조건 만족하는 칸 개수: 1보다 클 경우 2번 조건 탐색
                if cnt1 == 1:   # cnt 1일때 x, y 값 저장: 1번 조건으로 정해질 경우!!
                    x1, y1 = x, y
                
                graphNextCond[y][x] = True
            else:                              # 1번 조건 만족하지 않을 경우, False
                graphNextCond[y][x] = False
    # print('cnt1 값: ', cnt1)
    if cnt1 == 1:   # 1번 조건으로 끝나는 경우
        graph[y1][x1] = stu
        graphLike[y1][x1] = stuLike

    else:           # 2번 조건 이상 가야 할 경우
        ## 2번 조건
        maxCntEmpty = 0 # max 인접한 칸이 빈칸인 칸의 수
        subSubGraph = [[0 for _ in range(n)] for _ in range(n)]     # 인접한 칸에 빈칸 수
        for y in range(n):      
            for x in range(n):
                cntEmpty = 0
                if graphNextCond[y][x] and graph[y][x] == 0:     # 1번 조건 만족하는 칸, 비어있는 칸 중
                    for j in range(4):      # 인접한 4칸에 빈 칸수
                        if 0<=y+dy[j]<n and 0<=x+dx[j]<n:
                            nx = x + dx[j]
                            ny = y + dy[j]
                            if graph[ny][nx] == 0:
                                cntEmpty += 1
                    if maxCntEmpty < cntEmpty:
                        maxCntEmpty = cntEmpty
                    subSubGraph[y][x] = cntEmpty
        # print('subSubGraph: ', subSubGraph)
        cnt2 = 0
        x2, y2 = -1, -1
        stop = False
        for y in range(n):
            for x in range(n):
                if subSubGraph[y][x] == maxCntEmpty and graph[y][x] == 0:
                    x2, y2 = x, y
                    stop = True
                    break
            if stop:
                break

        graph[y2][x2] = stu
        graphLike[y2][x2] = stuLike
    # print('graphNextCond: ', graphNextCond)
#     print('graph: ', graph)

# print('graph: ', graph)
# print('graphLike: ', graphLike)

ans = 0
for y in range(n):
    for x in range(n):
        subAns = 0
        for j in range(4):
            if 0<=y+dy[j]<n and 0<=x+dx[j]<n:
                nx = x + dx[j]
                ny = y + dy[j]
                if graph[ny][nx] in graphLike[y][x]:
                    subAns += 1
        if subAns == 0:
            ans += 0
        elif subAns == 1:
            ans += 1
        elif subAns == 2:
            ans += 10
        elif subAns == 3:
            ans += 100
        elif subAns == 4:
            ans += 1000

print(ans)
```
빡센 구현문제, 1, 2, 3번 조건을 차례차례 따져가며 자리 배치를 하면 된다. 3번 조건의 경우 for문을 돌면서 자동으로 정해지기에 따로 지정하지 않아도 된다. 
### 의견
예제 및 반례 케이스까지 모두 통과하여 풀었다고 생각했지만.. 틀렸다. 왜 틀렸을까.. 아기 상어 문제처럼... 혼란스럽다. 4시간은 투자한 것 같은데 뭐가 부족했던걸까


## 트럭 주차
https://www.acmicpc.net/problem/2979
### 문제풀이
```python
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
graph = [0 for _ in range(101)]
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start + 1, end + 1):
        graph[i] += 1

ans = 0
for i in range(1, 101):
    if graph[i] == 1:
        ans += a
    elif graph[i] == 2:
        ans += b * 2
    elif graph[i] == 3:
        ans += c * 3

print(ans)
```
1대 있을 때, 2대 있을 때, 3대 있을 때의 시간을 각각 구해 a, b, c에 곱해주면 된다.
### 의견
1분당 a, b, c원 이므로 start 시간에서 1을 더해서 계산해야 하고, 한 대당 a, b, c원이므로 b, c원을 곱할 땐 각각 2, 3을 곱한 값을 더해줘야 한다.