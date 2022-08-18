# Solving

## 숨바꼭질
https://www.acmicpc.net/problem/1697
### 문제풀이
```python
from collections import deque

n, k = map(int, input().split())
visited = [False for _ in range(100001)]

temp = deque([(n, 0)])
visited[n] = True

while temp:
    # x: 수빈이 위치
    # cnt: 수빈이가 x위치에 있을 때까지 흐른 시간
    x, cnt = temp.popleft()
    # 가장 처음에 수빈이와 동생의 위치가 같을 경우 0초
    if x == k:
        print(0)
        break
    if x + 1 == k or x - 1 == k or x * 2 == k:
        print(cnt + 1)
        break
    else:
        if 0 <= x - 1 <= 100000 and visited[x - 1] == False:
            temp.append((x - 1, cnt + 1))
            visited[x - 1] = True
        if 0 <= x + 1 <= 100000 and visited[x + 1] == False:
            temp.append((x + 1, cnt + 1))
            visited[x + 1] = True
        if 0 <= x * 2 <= 100000 and visited[x * 2] == False:
            temp.append((x * 2, cnt + 1))
            visited[x * 2] = True
```
bfs 알고리즘을 사용해 수빈이의 위치에 대해 1초 후에 이동할 수 있는 위치를 모두 queue에 넣는다. 이 때, 얼마만큼의 시간이 흘렀는지 확인하기 위해 수빈이의 위치와 그 위치에 있을 때까지 흐른 시간을 함께 입력한다.
### 의견
처음에 그리디 알고리즘인줄 알고 접근하다가 점점 복잡해지는 것을 느꼈다. 문제 자체의 힌트를 보고 bfs 알고리즘으로 접근했는데, 수빈이가 x의 위치에 있을 때 몇 초가 흘렀는지를 확인할 방법을 찾기가 까다로웠다. 
전형적인 그래프 탐색 문제인 것 같은데 아직 숙련도가 좀 부족한 것 같다. 예외처리의 경우에도 처음에 수빈이와 동생의 위치가 같을 경우, 수빈이의 위치가 0에서 시작할 경우를 고려하지 않았어서 이를 해결하는데 시간이 좀 걸렸다.