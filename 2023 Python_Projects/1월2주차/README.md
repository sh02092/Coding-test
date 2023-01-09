# Solving

## 회의실 배정 2
https://www.acmicpc.net/problem/19621
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
time = [0]  # 회의 진행 시간
total = [0]     # 최대 인원
for _ in range(n):
    a, b, t = map(int, input().split())
    time.append(t)
time.append(0)

# i 번째 회의를 진행할 경우 
# (i - 1)번째 최댓값이었던 회의 시간과 비교하여 
# 큰 경우를 i번째 회의 시간의 최댓값으로 
total.append(time[1])
for i in range(2, n + 1):   
    total.append(max(total[i - 2] + time[i], total[i - 1]))

print(total[-1])
```
점화식을 세워 회의 진행 가능한 최대 인원을 구한다.
### 의견
많이 접했던 문제였지만, 매번 점화식을 생각하지 못해 구글의 힘을 빌렸던 문제였다. 하지만 이번 기회에 끝까지 생각해보며 풀어보고 싶은 마음에 계속 고민과 고민을 반복한 끝에 점화식을 생각해낼 수 있었고, 다음에 이런 문제가 나온다면 더욱 빠른 시간 안에 해결할 수 있을 것 같다.