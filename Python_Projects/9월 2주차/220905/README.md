# Solving

## 탑
https://www.acmicpc.net/problem/2493
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack = []
temp = [0] * n

# 전체 탑을 돌며
for i in range(n):
    t = tower[i]
    # stack이 존재하고, 스택의 가장 마지막 원소값이 현재 탑보다 작으면
    # 무시한다
    while stack and tower[stack[-1]] < t:
        stack.pop()
    # stack이 존재하면,
    # 스택의 가장 마지막 원소값 + 1 높이의 탑 레이저 수신
    if stack:
        temp[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, temp))))
```
탑을 돌며 stack에 넣고, 다음 탑을 돌 때 높이가 stack의 가장 마지막 원소보다 높을 경우 stack 마지막 원소를 pop() 하는 것을 stack이 비거나 마지막 원소 값이 현재 탑의 높이보다 높을 때까지 반복하여 시간 복잡도를 줄인다.
### 의견
처음에 시간 초과가 뜰 것을 예상했지만 완전탐색으로 접근했다. 시간 초과가 발생했고, 고민을 좀 했다. 비교를 최대한 안하는 방법... 꾸역꾸역 찾았다 생각했지만 여전히 시간 초과 발생! 구글링을 했다. 현재 탑에서 스택의 마지막 원소값과 비교하여 현재 탑보다 낮다면 스택을 없애며 비교하면 해결된다.. 혼자 생각하기 쉽지 않을 것 같은 문제였다. 다시 나오면 꼭 혼자 풀어봐야겠다.