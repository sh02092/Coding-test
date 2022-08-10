# https://www.acmicpc.net/problem/18430
# 무기 공학- BJ_18430

n, m = map(int, input().split())
tree_map = [list(map(int, input().split())) for _ in range(n)]
use_map = [[False for _ in range(m)] for _ in range(n)]

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# case 1
dx_1, dy_1 = [-1, 0], [0, 1]
# case 2
dx_2, dy_2 = [-1, 0], [0, -1]
# case 3
dx_3, dy_3 = [1, 0], [0, -1]
# case 4
dx_4, dy_4 = [1, 0], [0, 1]

