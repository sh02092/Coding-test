from collections import deque
import sys
input = sys.stdin.readline

num_i, num_j = map(int, input().split())
graph = []
num_count = []
temp = [[False for _ in range(num_j)] for _ in range(num_i)]
for _ in range(num_i):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while 1:
    q = deque()
    q.append([0, 0])
    count = 0
    total_count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < num_i and 0 <= ny < num_j and temp[nx][ny] == False:
                temp[nx][ny] = True
                if graph[nx][ny] == 0:
                    q.append([nx, ny])
                elif graph[nx][ny] == 1:
                    count += 1
                    graph[nx][ny] = 0

    num_count.append(count)

    for i in range(num_i):
        for j in range(num_j):
            if temp[i][j] == True:
                temp[i][j] = False
                total_count += 1

    if count == 0:
        break

if num_count[0] == 0:
    print(0)
else:
    print(len(num_count) - 1)
print(num_count[-2])