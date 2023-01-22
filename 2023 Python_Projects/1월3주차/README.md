# Solving

## 센서
https://www.acmicpc.net/problem/2212
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int,input().split()))
sensor.sort()

array = []
for i in range(n - 1):
    array.append(sensor[i + 1] - sensor[i])

array.sort()

print(sum(array[:n - k]))
```
### 의견
구현으로 풀어내려 했지만.. 해결하지 못했다.
구글링을 해보니 골드라고 하기엔 쉬운 문제였다.
다음에 다시 나오면 풀 수 있을까?