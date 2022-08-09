# Solving

## 게리맨더링 2
https://www.acmicpc.net/problem/17779
### 문제풀이
```python

```

### 의견



## 최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939
### 문제풀이
```python
def solution(s):
    answer = ''
    num_list = list(map(int, s.split(' ')))
    min_num = min(num_list)
    max_num = max(num_list)
    answer = str(min_num) + " " + str(max_num)
    return answer

s = input()
print(solution(s))
```
min, max 함수 사용, 출력할 때 str() 사용해 문자열로 바꾸고 ' ' 추가하여 출력한다.
### 의견
파이썬에서 정말 쉬운 문자열 문제


## 오큰수
https://www.acmicpc.net/problem/17298
### 문제풀이
```python
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

big = [-1 for _ in range(n)]
stack = deque()

for i in range(n):
    while stack and (stack[-1][0] < A[i]):
        temp, temp_idx = stack.pop()
        big[temp_idx] = A[i]
    stack.append([A[i], i])

print(*big)
```
A 배열의 순서대로 넣는데, 넣는 수가 이미 들어있는 스택 값보다 클 경우 스택이 빌 때까지 pop하며 오큰수를 큰 값으로 바꾼다. pop할 때 pop 하는 값들의 오큰수는 앞의 큰 값이다.
### 의견
O(n^2) 의 문제를 O(n)에 가깝게 만드는 시간 복잡도를 해결하는데 있어서 까다로웠던 문제였다.