# Solving

## 기타리스트- BJ_1495
https://www.acmicpc.net/problem/1495
### 문제풀이
```python
from collections import deque
import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
# (n x m) 의 deque으로 만든 n줄짜리 list
temp = deque([[False for _ in range(m + 1)] for _ in range(n + 1)])
temp[0][s] = True

# list 한줄씩 넘어가면서 v[i - 1] 빼고, 더하며 
# 조건 만족하면 True 체크
for i in range(1, n + 1):
    for j in range(m + 1):
        if temp[i - 1][j] == True:
            if j - v[i - 1] >= 0:
                temp[i][j - v[i - 1]] = True
            if j + v[i - 1] <= m:
                temp[i][j + v[i - 1]] = True

total = deque()
# 가장 마지막 list에 대해 True 일 경우 total list에 입력
for i in range(m + 1):
    if temp[-1][i] == True:
        total.append(i)
# total list의 최댓값 출력
if total:
    print(max(total))
# total이 비어있으면, -1 출력
else:
    print(-1)

```
n x m의 n줄짜리 list를 만들어 n번 돌 동안 list 한 줄씩 넘어가며 조건 만족하면 길이 m의 list에 True 체크한다. 이후 가장 마지막 list에 대해 True일 경우 total list에 입력하여 total list의 최댓값을 출력한다. total list가 비어있을 경우 -1을 출력한다.
### 의견
스택을 사용하여 조건을 만족하는 경우 스택에 넣고 하나씩 뽑아서 조건 비교하여 스택을 채우는 방법으로 코딩을 진행했었는데, 메모리 초과가 발생하여 고민하다가 반례를 찾아봤다. 반례를 적용시킨 결과 너무 오래 걸려 결국 모범 답안을 찾아봤는데.. 전혀 생각지도 못한 메모리 활용... 감탄이 나온다...
