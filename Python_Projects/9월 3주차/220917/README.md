# Solving

## 로또
https://www.acmicpc.net/problem/6603
### 문제풀이
```python
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

while 1:
    k_s = deque(deque(map(int, input().split())))
    if k_s[0] == 0:
        break

    k = k_s[0]
    k_s.popleft()
    sCombK = list(combinations(k_s, 6))
    for i in sCombK:
        print(*i)
    print()
```
순열을 import 하여 가능한 모든 경우의 수 출력한다.
### 의견
순열을 사용한 간단한 문제였다. 모든 경우의 수를 직접 출력해볼까 생각도 했지만 다음에 비슷한 문제가 나오면 해보는걸로..