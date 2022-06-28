import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
# m * n list 선언(0행 0열 제외)
graph = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    # list 마지막 원소에 \n 들어감
    a = list(input())
    
    # for 문을 돌릴 때, len(a) - 1 만큼 돌려야 함
    for j in range(1, len(a)):
        graph[i][j] = a[j - 1]

# 서 동 남 북
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 정수로 바꿔주는 부분
graph[1][1] = 1

# deque에 list 형태로 넣기
q = deque([(1, 1)])

while q:
    # deque에 list 형태로 지우고,
    # x = q[0][0], y = q[0][1]
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 미로 빠져나가지 못하는 조건문
        if nx > 0 and ny > 0 and nx <= n and ny <= m:
            # 결국엔 가장 최단 경로의 미로 값이 (n, m)에 들어가있어서
            # 더 긴 경로의 경우, if문 들어가지 못함
            if graph[nx][ny] == '1':
                q.append((nx, ny))
                # 정수로 바꿔주는 부분이 있어서 정수 더하기 가능
                graph[nx][ny] = graph[x][y] + 1
                # print(nx, ny)
                # print(graph[nx][ny])
                # print(q)

print(graph[n][m])