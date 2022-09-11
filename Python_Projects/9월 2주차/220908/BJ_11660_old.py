import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
temp = [[0 for _ in range(n)] for _ in range(n)]
el_total = 0

for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(n):
        el_total += graph[i][j]
        temp[i][j] = el_total

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1==x2 and y1==y2:
        print(graph[x1 - 1][y1 - 1])
    else:
        print(temp[x2 - 1][y2 - 1] - temp[x1 - 1][y1 - 1])

