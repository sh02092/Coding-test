from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = []
check = [[False] * m for _ in range(n)]
q = deque()

for x in range(n):
    for y in range(m):
        count = 0
        if graph[x][y] == 1 and check[x][y] == False:
            count += 1
            q.append([x, y])
            check[x][y] = True
            while q:
                x_, y_ = q.popleft()
                for i in range(4):
                    nx = x_ + dx[i]
                    ny = y_ + dy[i]
                    if nx >= 0 and ny >= 0 and nx < n and ny < m: 
                        if check[nx][ny] == False and graph[nx][ny] == 1:
                            check[nx][ny] = True
                            q.append([nx, ny])
                            count += 1
        if count > 0:
            total.append(count)
if len(total) > 0:
    print(len(total))
    print(max(total))
else:
    print(0)
    print(0)