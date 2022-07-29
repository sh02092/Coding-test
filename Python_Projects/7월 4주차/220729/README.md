# Solving

## 회의실 배정- BJ_1931
https://www.acmicpc.net/problem/1931
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
q = []
count = 0
end = 0
for _ in range(n):
    q.append(list(map(int, input().split())))

q = sorted(q, key = lambda x:x[0])
q = sorted(q, key = lambda x:x[1])

for i, j in q:
    if i >= end:
        count += 1
        end = j
print(count)
```
회의가 시작하자마자 끝나는 경우도 있으므로 시작하는 시간 기준 정렬을 먼저 진행하고 이후 끝나는 시간 기준 정렬을 한다. end를 기준으로 end보다 이후에 시작하는 회의를 선택해 count 및 회의 끝나는 시간을 end로 지정한다.
### 의견
그리디 알고리즘, 아직 익숙하지 않은 알고리즘으로 많은 유형의 문제를 풀어봐야 할 것 같다. 
탐욕적인 알고리즘 자체를 왜 사용하는지 아직 이해가 잘 안된다...