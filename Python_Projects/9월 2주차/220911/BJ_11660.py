# https://www.acmicpc.net/problem/11660
# 구간 합 구하기- BJ_11660

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
graph[0] = [0 for _ in range(n + 1)]
for i in range(1, n +1):
    graph[i] = [0] + list(map(int, input().split()))

# 행의 합
for i in range(1, n + 1):
    for j in range(1, n):
        graph[i][j + 1] += graph[i][j]

# 열의 합
for j in range(1, n + 1):
    for i in range(1, n):
        graph[i + 1][j] += graph[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(graph[x2][y2] - graph[x1 - 1][y2] - graph[x2][y1 - 1] + graph[x1 - 1][y1 - 1])