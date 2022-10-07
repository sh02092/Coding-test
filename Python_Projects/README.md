### Python

## 문자열
```python
string_1 = 'hello world'        # 문자열 선언
print(string_1.count('l'))      # 문자열에서 특정 문자 개수 출력

print(string_1.find('e'))       # 문자열에서 첫번째로 있는 특정 문자 index 출력, 존재하지 않으면 -1 출력
print(string_1.index('e'))      # 위와 동일하게 첫번째로 있는 특정 문자 index 출력, 존재하지 않으면 오류 발생

print(string_1.upper())         # 문자열 모두 대문자로 변환하여 출력
print(string_1.lower())         # 문자열 모두 소문자로 변환하여 출력

print(string_1.lstrip())        # 문자열 왼쪽의 한 칸 이상의 공백 모두 삭제하여 출력
print(string_1.rstrip())        # 문자열 오른쪽의 한 칸 이상의 공백 모두 삭제하여 출력

print(string_1.replace('world', 'hello'))   # 문자열의 특정 값 다른 값으로 치환하여 출력

print(string_1.split())         # 문자열을 공백(스페이스, 탭, 엔터, ...) 기준 나눠 list로, 출력
print(string_1.split('o'))      # 문자열을 'o' 기준 나눠 list로, 출력

print(':'.join(string_1))       # 문자열의 모든 문자 사이에 ':' 추가하여 출력

print(string_1)
```


## 리스트
```python
list_1 = list()
list_1.append(10)   # list 가장 뒤에 10 넣기
list_1.append(9)    # list 가장 뒤에 9 넣기
list_1.append(8)    # list 가장 뒤에 8 넣기
list_1.append(7)    # list 가장 뒤에 7 넣기
list_1.append(6)    # list 가장 뒤에 6 넣기
list_1.append(5)    # list 가장 뒤에 5 넣기
list_1.append(4)    # list 가장 뒤에 4 넣기
list_1.append(3)    # list 가장 뒤에 3 넣기
list_1.append(2)    # list 가장 뒤에 2 넣기
list_1.append(1)    # list 가장 뒤에 1 넣기
list_1.append(0)    # list 가장 뒤에 0 넣기

list_1.pop()        # list 가장 뒤 원소 삭제
a = list_1.pop(0)   # list 0번째 원소 삭제하여 a에 대입
del list_1[2]       # list 2번째 원소 지우기
del list_1[:2]      # list 0번째 원소부터 1번째 원소까지 지우기
list_1.remove(1)    # list에서 첫번째로 있는 1 지우기
print(list_1[:2])   # list 0번째 원소부터 1번째 원소까지 출력
print(list_1[1:3])  # list 1번째 원소부터 2번째 원소까지 출력
print(list_1[3:])   # list 3번째 원소부터 마지막 원소까지 출력

list_1.insert(0, 1) # list 0번째에 1 넣기

list_2 = [-1, -2, -3]
list_3 = list_1 + list_2    # list_1 뒤에 list_2 연결해 list_3에 대입
list_1.extend(list_2)   # list_1 뒤에 list_2 연결

len(list_1)         # list의 길이
listCopy = list_3.copy()    # listCopy에 list_3 깊은 복사하여 대입
print(listCopy.reverse())   # listCopy 뒤집어 출력
print(listCopy.sort())      # listCopy 오름차순 정렬 후 출력
print(listCopy.sort(reverse = True))    # listCopy 내림차순 정렬 후 출력
print(listCopy.count(3))    # listCopy 리스트 안의 원소 중 3의 개수 출력
print(listCopy.index(3))    # listCopy 리스트 안의 원소 중 첫 번째로 있는 3의 위치 index 출력
print(listCopy.clear())     # listCopy 리스트 초기화 후 출력

list_4 = [1, 2, 1, 2, 1, 1, 1, 3]
print(set(list_4))          # list 중복 값 제거 후 출력, 집합 자료형, 값들의 순서 X
print(list(set(list_4)))    # 값들의 순서가 없으므로 index로 접근 불가능 -> list로 변환 후 접근
```


## 이분 탐색
```python
def binary_search(arr, target, min, max):
  min, max = 0, len(arr) - 1
    while min <= max:
        mid = (min + max) // 2
        if arr[mid] > target:
            max = mid - 1
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            min = mid + 1
    return -1
```

## DFS
```python
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
temp = [[False for _ in range(max_col)] for _ in range(max_row)]

def dfs(x, y, max_row, max_col):
    q = deque([(y, x)])
    while q:
        y_, x_ = q.popleft()
        temp[y_][x_] = True
        for i in range(4):
            ny = y_ + dy[i]
            nx = x_ + dx[i]
            if 0 <= ny < max_row and 0 <= nx < max_col and temp[ny][nx]:
                q.append(ny, nx)
                temp[ny][nx] = True
```


## Linked list
```python
class Node:
    def __init__(self):
        self.prev = -1 # 이전 노드 인덱스
        self.next = -1 # 다음 노드 인덱스
        self.is_delete = False # 삭제 여부

# 링크드리스트 초기화
node_list = [Node() for _ in range(n)] # 노드 리스트 생성
for i in range(n - 1):
    node_list[i].next = i + 1 # i 번째 노드의 next는 i+1
    node_list[i + 1].prev = i # i+1 번째 노드의 prev는 i
```
