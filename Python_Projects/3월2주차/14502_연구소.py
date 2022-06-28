# 브루트포스 + BFS
# 모든 경우의 수로 벽을 세운다.
# 안전영역 최대 크기를 출력한다.

from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs():
    # 깊은 복사, 내부 객체들까지 모두 새롭게 copy... 중요
    graph_ = copy.deepcopy(graph)
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph_[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dn[k]
            ny = y + dm[k]
            
            if nx >= 0 and ny >=0 and nx < n and ny < m:
                if graph_[nx][ny] == 0:
                    graph_[nx][ny] = 2
                    q.append([nx, ny]) 
    v = 0
    for i in range(n):
        v += graph_[i].count(0)
    count_v.append(v)


# 브루트포스로 모든 경우의수 다 돌아보는 재귀... 중요
def wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count + 1)
                graph[i][j] = 0


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

count_v = []
wall(0)

count_v = sorted(count_v)
print(count_v[-1])

# from collections import deque
# import copy

# def bfs():
#     queue = deque()
#     tmp_graph = copy.deepcopy(graph)
#     for i in range(n):
#         for j in range(m):
#             if tmp_graph[i][j] == 2:
#                 queue.append((i, j))

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if tmp_graph[nx][ny] == 0:
#                 tmp_graph[nx][ny] = 2
#                 queue.append((nx, ny))

#     global answer
#     cnt = 0

#     for i in range(n):
#         cnt += tmp_graph[i].count(0)

#     answer = max(answer, cnt)


# def makeWall(cnt):
#     if cnt == 3:
#         bfs()
#         return

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 makeWall(cnt+1)
#                 graph[i][j] = 0

# n, m = map(int, input().split())
# graph = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# for i in range(n):
#     graph.append(list(map(int, input().split())))

# answer = 0
# makeWall(0)
# print(answer)