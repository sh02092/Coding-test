# Solving

## 상근이의 여행
https://www.acmicpc.net/problem/9372
### 문제풀이
```python
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    n_graph = [[] for _ in range(n + 1)]
    count = 0
    for _ in range(m):
        a, b = map(int, input().split())
        n_graph[a].append(b)
        n_graph[b].append(a)
    visited = [False for _ in range(n + 1)]
    dfs = deque([1])
    visited[1] = True
    while dfs:
        x = dfs.popleft()
        count += 1
        for i in n_graph[x]:
            if visited[i] == False:
                dfs.append(i)
                visited[i] = True
    print(count - 1)
```
m번의 비행기 쌍을 각각 n_graph에 넣어 각 국가에서 이동할 수 있는 국가를 입력한다. 왕복이므로 a -> b, b -> a 모두 입력한다. dfs 알고리즘을 사용해 visited 체크를 하며 이동하지 않은 국가가 없을 때 count를 출력한다.
### 의견
어렵지 않았던 문제였다.


## 키패드 누르기
https://school.programmers.co.kr/learn/courses/30/lessons/67256
### 문제풀이
```python
def solution(numbers, hand):
    answer = ''
    
    left, l = '*', 4    # 현재 왼손위치: *, 4층
    right, r = '#', 4   # 현재 오른손위치: #, 4층
    temp = -1

    for i in numbers:
        number = (i - 1)

        if number == -1:    # 0일 경우
            temp = 4        # number 위치: 0, 4층
            dist_l = abs(temp - l)          
            dist_r = abs(temp - r)
            if left == '*': dist_l += 1
            elif left % 3 != 2: dist_l += 1   # 누르고자 하는 번호와 왼손의 위치 차이
            
            if right == '#': dist_r += 1
            elif right % 3 != 2: dist_r += 1  # 누르고자 하는 번호와 오른손의 위치 차이

            if dist_l > dist_r:
                answer += 'R'
                right, r = 0, 4
            elif dist_l < dist_r:
                answer += 'L'
                left, l = 0, 4
            else:

                if hand == 'right':
                    answer += 'R'
                    right, r = 0, 4
                else:
                    answer += 'L'
                    left, l = 0, 4
        elif number % 3 == 1:       # 2 or 5 or 8 일 경우
            temp = number // 3 + 1  # number 위치: i, temp층
            dist_l, dist_r = abs(temp - l), abs(temp - r)
            if left == '*': dist_l += 1
            elif left % 3 != 2 and left != 0: dist_l += 1   # 누르고자 하는 번호와 왼손의 위치 차이

            if right == '#': dist_r += 1
            elif right % 3 != 2 and right != 0: dist_r += 1  # 누르고자 하는 번호와 오른손의 위치 차이

            if dist_l > dist_r:
                answer += 'R'
                right, r = i, temp
            elif dist_l < dist_r:
                answer += 'L'
                left, l = i, temp
            else:
                if hand == 'right':
                    answer += 'R'
                    right, r = i, temp
                else:
                    answer += 'L'
                    left, l = i, temp
        elif number % 3 == 0:               # 1 or 4 or 7 일 경우
            answer += 'L'                   # 'L' 누르고
            left, l = i, number // 3 + 1    # 현재 왼손위치: i, (number // 3)층
        elif number % 3 == 2:               # 3 or 6 or 9 일 경우
            answer += 'R'                   # 'R' 누르고
            right, r = i, number // 3 + 1   # 현재 오른손위치: i, (number // 3)층
        
    return answer

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
print(solution(numbers, hand))
```
1, 4, 7일 경우엔 왼손, 3, 6, 9일 경우엔 오른손으로 누르고, 나머지 2, 5, 8, 0의 경우 누르기 직전의 왼손, 오른손과의 거리를 측정해 거리가 가까운 손으로 누르고 만약 거리가 같다면 오른손잡이면 오른손으로, 왼손잡이면 왼손으로 눌러 전체 numbers list를 모두 손으로 누른 answer list를 출력한다.
### 의견
1, 4, 7이나 3, 6, 9를 판별하는데는 어려움이 없었다. 하지만 첫 시작이 왼손은 '*', 오른손은 '#'인 부분과 2, 5, 8, 0의 경우 누르기 직전의 왼손, 오른손과의 거리 측정하는 부분, 2, 5, 8과 다른 0의 경우를 나눠서 구현하는 부분에서 까다로웠다. 풀고 난 후 level 1인 것을 보고 level 1에서 아직 쩔쩔대는 내 모습에 부족함을 많이 느꼈다.