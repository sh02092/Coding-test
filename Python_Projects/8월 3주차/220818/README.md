# Solving

## 표 편집
https://school.programmers.co.kr/learn/courses/30/lessons/81303
### 문제풀이
```python
from collections import deque

class Node:
    def __init__(self):
        self.prev = -1 # 이전 노드 인덱스
        self.next = -1 # 다음 노드 인덱스
        self.is_delete = False # 삭제 여부

def solution(n, k, cmd):
 
    # 1. 링크드리스트 초기화
    node_list = [Node() for _ in range(n)] # 노드 리스트 생성
    for i in range(n - 1):
        node_list[i].next = i + 1 # i 번째 노드의 next는 i+1
        node_list[i + 1].prev = i # i+1 번째 노드의 prev는 i
 
    # 2. 삭제된 노드를 저장할 스택
    del_stack = deque()
 
    # 3. 명령어 처리
    cur = k # 현재 가리키고 있는 노드의 인덱스
    for c in cmd:
 
        if len(c) > 1:
            c, move_size = c.split(' ')
            move_size = int(move_size)
 
        if c == "U":
            for i in range(move_size):
                cur = node_list[cur].prev # cur을 cur 노드의 prev로 교체
        elif c == "D":
            for i in range(move_size):
                cur = node_list[cur].next # cur을 cur 노드의 next로 교체
        elif c == "C":
            node_list[cur].is_delete = True # 현재 노드에 삭제 표시
            del_stack.append(cur) # 스택에 삭제된 노드 번호 추가
 
            prev_node = node_list[cur].prev # 이전 노드 번호
            next_node = node_list[cur].next # 다음 노드 번호
 
            if prev_node != -1: # 이전 노드가 있는 경우
                node_list[prev_node].next = next_node # 이전 노드의 next를 삭제된 노드가 가리키던 next로 교체
            if next_node != -1: # 다음 노드가 있는 경우
                node_list[next_node].prev = prev_node # 다음 노드의 prev를 삭제된 노드가 가리키던 prev로 교체
                cur = next_node # 가리키고 있는 노드를 next_node로 갱신
            else: # 만약 다음 노드가 없는 경우
                cur = prev_node # 가리키고 있는 노드를 prev_node로 갱신
 
        elif c == "Z":
            del_node = del_stack.pop() # stack의 가장 상위 요소를 가져옴
            node_list[del_node].is_delete = False # 해당 노드의 is_delete = False로 변경
 
            prev_node = node_list[del_node].prev # 삭제된 노드의 이전 노드
            next_node = node_list[del_node].next # 삭제된 노드의 다음 노드
 
            if prev_node != -1: # 이전 노드가 존재하는 경우
                node_list[prev_node].next = del_node # 이전 노드의 next를 현재 노드로 지정
            if next_node != -1:
                node_list[next_node].prev = del_node # 다음 노드의 prev를 현재 노드로 지정
 
    # 4. 삭제된 노드 판별
    answer = []
    for i in range(n):
        if node_list[i].is_delete: answer.append("X")
        else: answer.append("O")
    return "".join(answer)
```
linked-list를 만들어 모든 노드를 연결시킨다. 명령어에 따라 'U', 'D'일 경우 move_size만큼 가리키는 노드의 인덱스를 이동시킨다. 'C'일 경우 현재 가리키는 노드를 삭제하여 스택에 쌓고, 이전 노드와 다음 노드를 서로 연결시킨다. 'Z'일 경우 스택 가장 위 노드를 가져와 다시 연결시킨다. 마지막으로 삭제된 노드 판별을 위해 각 노드별로 삭제 여부를 판별한다.
### 의견
list를 만들어 pop(), insert(index, value) 를 사용해 구현했었다. 하지만 시간 복잡도와 효율성이 모두 너무 안좋게 나와 해결법을 찾기 위해 구글링을 했다. 결과는 링크드 리스트의 사용... 알고 있던 알고리즘이지만 너무 오랜만에 사용하고, 다시 느끼지만 카카오는 아직은 높은 벽인 것 같다.