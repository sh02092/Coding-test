# Solving

## 수 찾기
https://www.acmicpc.net/problem/1920
### 문제 풀이
```python
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
m_count = [0 for _ in range(len(m_list))]

n_list = sorted(set(n_list))

for i in range(len(m_list)):
    min = 0
    max = len(n_list) - 1
    while min <= max:
        mid = (min + max) // 2
        if m_list[i] == n_list[mid]:
            m_count[i] += 1
            break
        elif m_list[i] > n_list[mid]:
            min = mid + 1
        elif m_list[i] < n_list[mid]:
            max = mid - 1

for i in m_count:
    print(i)
```
n 개의 정수, m 개의 정수를 각각 입력한다. n 개의 정수에 대해 오름차순으로 정렬시킨 이후 m 개의 정수 각각에 대해 이분탐색 알고리즘을 적용해 같은 정수일 경우 m_count list를 증가시켜 존재하면 1, 존재하지 않으면 0을 출력한다.

### 의견
처음에는 n 개의 정수에 대해 모두 비교하는 코드를 짰는데, 결과적으로 시간 초과가 발생했다. 이분 탐색 알고리즘으로 시간 복잡도를 해결해야겠다는 생각이 들었고, 지금껏 풀어봤던 이분 탐색 알고리즘을 생각하여 풀 수 있었다.


## 수 정렬하기 2
https://www.acmicpc.net/problem/2751
### 문제풀이
```python
import sys
input = sys.stdin.readline
n = int(input())
n_ = [int(input()) for _ in range(n)]
n_ = sorted(n_)
for i in n_:
    print(i)
```
n 개의 정수를 입력하여 오름차순으로 정렬해 출력한다.

### 의견
단순히 입력 받고, 정렬하여 출력하면 되는 간단한 문제였다.


## 수 정렬하기 3
https://www.acmicpc.net/problem/10989
### 문제풀이
```python
import sys
input = sys.stdin.readline

n = int(input())

# 미리 list를 만들어놓는다.
# append를 사용할 경우 메모리 재할당이 이루어져 
# 속도 저하가 일어나고, 효율적이지 못하다.
n_ = [0 for _ in range(10001)]
for _ in range(n):
    n_[int(input())] += 1

for i in range(len(n_)):
    if n_[i] != 0:
        for _ in range(n_[i]):
            print(i)
```
위의 수 정렬하기 2와 같이 n 개의 정수를 list에 입력하는 방식이 아닌 미리 가질 수 있는 최대 크기의 list를 만들어 놓고 존재할 경우 count를 증가시키는 방식으로 진행한다.

### 의견
list에 append를 할 경우 메모리 재할당이 이루어져 속도 저하가 일어나는 것을 다음 링크에서 알 수 있었다.
https://wikidocs.net/21057


## 숫자 카드
https://www.acmicpc.net/problem/10815
### 문제풀이
```python
n = int(input())
n_ = list(map(int, input().split()))
m = int(input())
m_ = list(map(int, input().split()))

n_ = sorted(n_)
m_count = [0 for _ in range(len(m_))]

for i in range(len(m_)):
    min = 0
    max = len(n_) - 1
    while min <= max:
        mid = (min + max) // 2
        if m_[i] == n_[mid]:
            m_count[i] += 1
            break
        elif m_[i] > n_[mid]:
            min = mid + 1
        elif m_[i] < n_[mid]:
            max = mid - 1

for i in range(len(m_count)):
    print(m_count[i], end=" ")
```
n 개의 정수와 m 개의 정수를 입력한다. n 개의 정수 list에 대해 정렬하여 min, max를 설정하고, 이분 탐색 알고리즘을 통해 m 개의 정수와 비교한다.

### 의견
위의 수 찾기 문제와 동일한 방법인 이분 탐색 알고리즘을 통해 쉽게 해결할 수 있었다.


## 스택
https://www.acmicpc.net/problem/10828
### 문제풀이
```python
from collections import deque
import sys
input = sys.stdin.readline

n_ = deque()
for _ in range(int(input())):
    text = input().rstrip()
    if text[0] == 'p':
        if text[1] == 'u':
            n_.append(int(text[5:]))
        elif text[1] == 'o':
            if n_:
                print(n_[-1])
                n_.pop()
            else:
                print(-1)

    elif text[0] == 't':
        if n_:
            print(n_[-1])
        else:
            print(-1)
    elif text[0] == 's':
        print(len(n_))
    elif text[0] == 'e':
        if n_:
            print(0)
        else:
            print(1)
```
deque()를 선언하여 n만큼 명령어를 입력한다. 입력한 명령어에 대해 맨 앞 키워드를 조건으로 명령어에 대해 처리하는 프로그램을 작성한다.

### 의견
스택에 대해 알고 있어 쉽게 접근할 수 있고, 문제에서 주어진 조건만 빼먹지 않고 작성하면 코드 부분에서도 이해가 안되는 부분은 없었다.