# Solving

## 외계인의 기타 연주
https://www.acmicpc.net/problem/2841
### 문제풀이
```python
import sys
input = sys.stdin.readline

n, p = map(int, input().split())
push = [[0] for _ in range(n + 1)]
count = 0

for _ in range(n):
    n_, p_ = map(int, input().split())
    # n_, p_ 에 대해
    # n_번째 줄의 가장 높은 프렛보다 p_ 번째 프렛이 높다면
    # p_ 번째 프랫을 누르고, count 추가한다.
    if p_ > push[n_][-1]:
        push[n_].append(p_)
        count += 1
    # n_번째 줄의 가장 높은 프렛보다 p_번째 프랫이 낮다면
    # p_번째 프랫이 더 커질 때까지 누르고 있던 프랫을 떼고, count를 추가한다.
    else:
        while push[n_][-1] > p_:
            push[n_].pop()
            count += 1
    # 마지막 프랫이 p_ 프랫보다 낮다면
    # p_ 프랫을 누르고, count 추가한다.
        if push[n_][-1] != p_:
            push[n_].append(p_)
            count += 1

print(count)

# 960ms
```
누르고자 하는 프랫이 기존 눌려져있던 프랫중 가장 높은 프랫보다 높으면 누르고자 하는 프랫을 누른다. 낮으면 낮아질 때까지 누르고 있던 프랫을 뗀다. 떼거나 누를 때 count를 센다.
### 의견
어렵지 않은 문제라고 판단하여 전체 음과 음에 대한 프렛을 2차원 리스트로 만들어 누른 프렛에 대해 True를 걸어주는 방식으로 접근했다. 하지만 메모리 초과로 실패.. 프렛을 누를 때마다 리스트에 프렛을 추가해주는 방식으로 방식을 변경했다. 변경했더니 시간초과... 하지만 시간 초과의 문제는 쉽게 해결할 수 있었다. 당연히 가장 마지막 리스트에 눌려져 있는 프렛 값이 최대 프렛 값이므로 최댓값을 따로 비교해주지 않아도 된다는 것을 알고, 오름차순 정렬을 해주지 않아도 자동으로 오름차순 정렬 순으로 리스트가 정렬되어 있는 것을 알아 시간 복잡도를 줄이는데 도움이 되었다.


## 쿼드압축 후 개수 세기
https://school.programmers.co.kr/learn/courses/30/lessons/68936
### 문제풀이
```python
def quad(x, y, temp, answer, arr):
    bin_val = arr[x][y]    
    break_ = False
    for i in range(x, x + temp):
        if break_:
            break
        for j in range(y, y + temp):
            # bin_val과 값이 같지 않을 경우 break
            if arr[i][j] != bin_val:
                break_ = True
                break
    # 정사각형 영역을 4등분 하여 각 영역에 대해 다시 quad() 함수 실행
    if break_:
        temp_2 = temp // 2
        for i in range(x, x + temp, temp_2):
            for j in range(y, y + temp, temp_2):
                quad(i, j, temp_2, answer, arr)
    else:
        answer[bin_val] += 1
                

def solution(arr):
    answer = [0, 0]

    temp = len(arr)
    quad(0, 0, temp, answer, arr)


    return answer

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))
```
quad() 함수를 만들어 정사각형 영역에 대해 모든 수가 같지 않을 경우 정사각형 영역의 크기를 가로, 세로 모두 반으로 4개의 영역으로 나누어 각 영역에 대해 영역 안의 모든 수가 같을 때 까지 반복하여 사용한다.
### 의견
어렵지 않은 재귀함수를 사용한 문제였다.
하지만 파이썬에서 함수를 사용할 때 전역변수(global) 사용과, 함수 파라미터 설정이 아직 미숙하다. quad() 함수에 사용된 함수 파라미터로 x, y, temp, answer, arr의 모든 변수를 입력했는데.. 더욱 효율적으로 함수를 만들 수 있는 방법이 있을 것 같다..


## 요세푸스 문제
https://www.acmicpc.net/problem/1158
### 문제풀이
```python
n, k = map(int, input().split())
k -= 1
temp = [(i + 1) for i in range(n)]
answer = []
num = 0

for i in range(n):
    num += k
    # num이 남은 사람의 수보다 많다면
    # 사람의 수로 나눈 나머지 번째 사람이 다음 제거 타겟
    if num >= len(temp):
        num %= len(temp)
    answer.append(str(temp.pop(num)))
print("<",", ".join(answer)[:],">", sep='')
```
### 의견
어렵지 않은 알고리즘 문제였다.
하지만 출력 방식이 좀 까다로운 문제였다.