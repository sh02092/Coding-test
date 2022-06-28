import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x):
    temp[x] = True
    for i in range(1, n + 1):
        if graph[x][i] == True and temp[i] == False:
            dfs(i)

n, m = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = True
temp = [False] * (n + 1)

count = 0
for i in range(1, n + 1):
    if temp[i] == False:
        dfs(i)
        count += 1

print(count)