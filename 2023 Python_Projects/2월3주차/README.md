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