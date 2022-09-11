# https://www.acmicpc.net/problem/11660
# 구간 합 구하기 5- BJ_11660

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1 - 1, x2):
        for k in range(y1 - 1, y2):
            