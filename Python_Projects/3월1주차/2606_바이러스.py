from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    temp[v] = True
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        for i in range(1, num + 1):
            if graph[x][i] == True and temp[i] == False:
                temp[i] = True
                q.append(i)

def dfs(v):
    temp[v] = True
    for i in range(1, num + 1):
        if graph[v][i] == True and temp[i] == False:
            dfs(i)

num = int(input())
line = int(input())
graph = [[False] * (num + 1) for _ in range(num + 1)]
for i in range(line):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

temp = [False] * (num + 1)

#bfs(1)
dfs(1)
print(temp.count(True) - 1)