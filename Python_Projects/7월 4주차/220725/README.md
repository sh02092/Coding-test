# Solving

## 크레인 인형뽑기 게임- PG_64061
https://school.programmers.co.kr/learn/courses/30/lessons/64061
### 문제풀이
```python
def solution(board, moves):
    answer = 0
    temp = []
    len_1 = 0
    # moves 리스트 값에 해당하는 수에 대해
    for i in moves:
        i -= 1
        for j in range(len(board[0])):
            # board 리스트 값이 0이면 다음 board 리스트 값 비교
            # 0이 아니면 temp 스택에 넣고, board 리스트 값 0으로
            if board[j][i] == 0:
                continue
            temp.append(board[j][i])
            board[j][i] = 0
            # temp 스택의 크기가 2 이상이면
            # 스택의 가장 윗 원소 2개의 값이 같으면
            # len_1보다 스택의 길이가 길 때까지
            # 같은 원소 2개 지우고 answer 2 키우기
            if len(temp) >= 2:
                if temp[-1] == temp[-2]:
                    while len_1 < len(temp):
                        temp.pop()
                        temp.pop()
                        answer += 2
                        len_1 = len(temp)
            break
    return answer

board = []
for i in range(int(input())):
    board.append(list(map(int, input().split())))
moves = list(map(int, input().split()))
print(solution(board, moves))
```
moves 리스트 값에 해당하는 board 리스트 값 중 0이 아닌 가장 위에 있는 값을 temp 스택에 넣는다. 
스택의 크기가 2보다 클 때 가장 마지막에 들어온 2개의 값이 같으면 지우고, answer를 2 증가시킨다. 
더이상 지워지지 않을 때 까지 지우기를 반복한다. 
### 의견
list와 stack을 잘 이용하여 어렵지 않았던 문제였다.


## 리모컨- BJ_1107
https://www.acmicpc.net/problem/1107
### 문제풀이
```python
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = deque(map(int, input().split()))
min_count = abs(100 - n)

# 가능한 모든 경우의 수에 대해
# 고장난 숫자가 포함된 채널을 제외하고
# 가장 적게 리모콘을 누른 경우
for i in range(1000001):
    i = str(i)
    for j in range(len(i)):
        if int(i[j]) in broken:
            break
        elif j == len(i) - 1:
            min_count = min(min_count, abs(int(i) - n) + len(i))
print(min_count)
```
고장난 숫자가 포함된 채널을 제외한 가능한 모든 경우의 수에 대해 가장 리모콘을 적게 누른 경우를 찾는 브루트포스 알고리즘이다.
### 의견
브루트포스 알고리즘으로 풀어야겠다는 생각을 하기까지 시간이 조금 걸렸고, 거르고 거른 이후의 경우의 수가 아닌 정말 전체의 경우의 수를 모두 비교하여 풀어야겠다는 생각을 하기가 쉽지 않았다.


## 킹- BJ_1063
https://www.acmicpc.net/problem/1063
### 문제풀이
```python
king, rock, n = map(str, input().split())
n = int(n)

# 0 번째 행 = -1  / 7 번째 행 = -8    -->   y축
# 0 번째 열 = A:0 / 7 번째 열 = H:7   -->   x축
king_x = ord(king[0]) - 65
king_y = -int(king[1])
rock_x = ord(rock[0]) - 65
rock_y = -int(rock[1])

#     R,  L, B, T,  RT, LT, RB, LB 
dx = [1, -1, 0,  0,  1, -1,  1, -1]
dy = [0,  0, 1, -1, -1, -1,  1,  1]
temp = {'R':0, 'L':1, 'B':2, 'T':3, 'RT':4, 'LT':5, 'RB':6, 'LB':7}

for _ in range(n):
    moves = input()
    idx = temp[moves]
    # 이동했을 때 체스판을 넘어갈 경우 이동하지 않고,
    # 체스판을 넘어가지 않을 경우 이동
    if king_x + dx[idx] > 7 or king_x + dx[idx] < 0 or king_y + dy[idx] > -1 or king_y + dy[idx] < -8:
        continue
    king_x += dx[idx]
    king_y += dy[idx]

    # 이동했을 경우 돌과 같은 좌표에 위치할 경우 
    # 돌이 이동할 때 체스판을 넘어갈 경우 이동하지 않고, 왕 또한 이동하기 전으로 돌아가고,
    # 체스판을 넘어가지 않을 경우 이동
    if king_x == rock_x and king_y == rock_y:
        if rock_x + dx[idx] > 7 or rock_x + dx[idx] < 0 or rock_y + dy[idx] > -1 or rock_y + dy[idx] < -8:
            king_x -= dx[idx]
            king_y -= dy[idx]
            continue
        rock_x += dx[idx]
        rock_y += dy[idx]

print(chr(king_x + 65) + str(-king_y))
print(chr(rock_x + 65) + str(-rock_y))
```
x, y 축 각각으로 이동하는 dx, dy 리스트, 각 이동하는 방향을 의미하는 temp 딕셔너리를 사용해 이동했을 경우 체스판을 넘어가는 경우와 넘어가지 않는 경우로 나눈다.
넘어갔을 경우에는 돌의 좌표와 비교해 같은 좌표일 경우 돌이 왕과 동일한 방향으로 이동해야 하는데 이 때에도 체스판을 넘어가는 경우와 넘어가지 않는 경우로 나눠 해결한다.
### 의견
구현 문제인 것은 문제를 읽고 바로 알았지만, 문제의 조건들을 모두 일일히 구현하려다 보니 빼먹는 조건들이 있었다. 
좌표계에서 좌표를 이동시키는 문제인 만큼 dx, dy 리스트를 활용해 조건을 모두 만족할 수 있게끔 코드를 효율적으로 짜는데 시간이 좀 필요한 문제였다.