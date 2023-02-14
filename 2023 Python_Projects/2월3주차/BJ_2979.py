# https://www.acmicpc.net/problem/2979
# 트럭 주차- BJ_2979

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
graph = [0 for _ in range(101)]
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start + 1, end + 1):
        graph[i] += 1

ans = 0
for i in range(1, 101):
    if graph[i] == 1:
        ans += a
    elif graph[i] == 2:
        ans += b * 2
    elif graph[i] == 3:
        ans += c * 3

print(ans)