from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x)
    temp[x] = True
    while q:
        y = q.popleft()
        for i in range(1, n + 1):
            if graph[y][i] == True and temp[i] == False:
                temp[i] = True
                q.append(i)
        


n, m = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = True
temp = [False] * (n + 1)
count = 1

for i in range(2, n + 1):
    bfs(i - 1)
    a = temp.count(True)
    bfs(i)
    b = temp.count(True)
    if a != b:
        count += 1
    

print(count)

