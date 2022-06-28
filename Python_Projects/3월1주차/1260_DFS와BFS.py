# from collections import deque
# import sys
# read = sys.stdin.readline

# def bfs(v):
#     q = deque()
#     q.append(v)
#     visit_list[v] = 1
#     while q:
#         v = q.popleft()
#         print(v, end = " ")
#         for i in range(1, n + 1):
#             if visit_list[i] == 0 and graph[v][i] == 1:
#                 q.append(i)
#                 visit_list[i] = 1

# def dfs(v):
#     visit_list2[v] = 1
#     print(v, end = " ")
#     for i in range(1, n + 1):
#         if visit_list2[i] == 0 and graph[v][i] == 1:
#             dfs(i)

# n, m, v = map(int, read().split())
# visit_list = [0] * (n + 1)
# visit_list2 = [0] * (n + 1)

# # (n + 1, n + 1) 크기의 0으로 초기화된 list 생성
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# for i in range(m):
#     a, b = map(int, read().split())
#     graph[a][b] = graph[b][a] = 1

# dfs(v)
# print()
# bfs(v)

from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    visit[v] = True
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visit[i] == False and graph[v][i] == True:
                visit[i] = True
                q.append(i)

def dfs(v):
    visit[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if visit[i] == False and graph[v][i] == True:
            dfs(i)

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
visit = [False] * (n + 1)

dfs(v)
visit = [False] * (n + 1)
print()
bfs(v)

