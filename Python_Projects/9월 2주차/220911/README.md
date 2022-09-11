# Solving

## 구간 합 구하기 5
https://www.acmicpc.net/problem/11660
### 문제풀이
```python
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
```
행, 열의 구간합을 더해 graph list를 재구성하고, (x2, y2) 까지의 합에서 (x1, y2) 까지의 구간과 (x2, y1) 까지의 구간을 빼고, (x1, y1) 까지의 구간을 다시 더해 원하는 구간에서의 list 원소 합을 구한다.
### 의견
그래프에서 구하고자 하는 구간 전체를 돌며 하나하나 더하는 식으로 구성을 했지만 시간초과가 발생했다. 쉽게 풀 수 있을 것이라 생각하여 계속 고민을 했지만.. 떠오르는 방법이 없었고 결국 찾아봤는데 헉... 정말 쉬운 문제였다. 행, 열 각각의 구간합을 구해 범위 안의 값을 구하는 문제... 초등학교때 사각형 안의 사각형 넓이를 구할 때 구하는 방법과 비슷하게 접근하면 쉽게 풀리는 문제였다.