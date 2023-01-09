# https://softeer.ai/practice/info.do?idx=1&eid=409
# 장애물 인식 프로그램- Softeer_409
from collections import deque
import sys
input = sys.stdin.readline

# dfs
def dfs(x, y):
    q = deque([(y, x)])
    cnt = 1
    while q:
        y_, x_ = q.popleft()
        for i in range(4):
            if 0<=y_+dy[i]<n and 0<=x_+dx[i]<n:
                ny = y_ + dy[i]
                nx = x_ + dx[i]
                if graph[ny][nx] == '1':
                    temp[ny][nx] = True
                    cnt += 1
                    q.append((ny, nx))
    return cnt

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
graph = list()
temp = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    graph.append(input())

# print(graph[0][0])
# print(temp)

ans = []
for i in range(n):
    for j in range(n):
        if (graph[i][j] == '1') and (temp[i][j] == False):
            ans.append(dfs(i, j))

print(len(ans))
ans.sort()
for i in ans:
    print(i)