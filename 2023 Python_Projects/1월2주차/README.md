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