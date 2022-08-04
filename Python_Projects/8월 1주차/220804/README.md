# Solving

## 양궁대회- PG_92342
https://school.programmers.co.kr/learn/courses/30/lessons/92342
### 문제풀이
```python
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    # x: 어피치, y: 라이언

    y_shoot = list(combinations_with_replacement(range(0, 11), n))
    max_score = 0

    for y in y_shoot:
        y_info = [0 for _ in range(11)]
        x_score = 0
        y_score = 0
        for i in y:
            y_info[10 - i] += 1
        for i in range(len(info)):
            if info[i] == y_info[i] == 0:
                continue
            elif info[i] >= y_info[i]:
                x_score += (10 - i)
            elif info[i] < y_info[i]:
                y_score += (10 - i)
        total_score = y_score - x_score
        if max_score < total_score:
            max_score = total_score
            answer = y_info
        elif max_score > 0 and max_score == total_score:
            for i in reversed(range(11)):
                if answer[i] > y_info[i]:
                    break
                elif answer[i] < y_info[i]:
                    answer = y_info
                    break
    return answer

info = [1,0,0,0,0,0,0,0,0,0,0]
n = sum(info)
print(solution(n, info))
```
11개의 점수 중 5개를 고르는 가능한 모든 경우의 수를 콤비네이션 연산을 통해 구해 y_info 리스트에 넣어 info 리스트와 비교하며 어피치, 라이언의 점수를 구하고, 점수가 커질 때마다 max_score 값, answer 리스트를 초기화한다. 이때 max_score 값과 라이언, 어피치 점수 차이가 같을 경우 answer, y_info 리스트를 뒤에서부터 비교하며 작은 점수의 수가 큰 경우를 answer 리스트로 택한다.
### 의견
브루트 포스 알고리즘으로 완전 탐색을 하는 문제라는 것은 파악하고 있었다. 하지만 어피치와 라이언의 info 리스트로 비교를 하려다 보니 오랜 삽질 끝에 해결하지 못하였고, 결국 어떤 방식으로 접근하는지에 대한 알고리즘을 봤다. 역시 카카오.. 문제를 정말 잘 만드는 것 같다. 활을 쏘는 경우의 수를 모두 구해 그에 맞는 라이언의 info 리스트를 만들어 비교하는 방법으로 해결할 수 있었다. 
여기에 더해 파이썬의 itertools 라이브러리를 알게 되었는데, 이는 조합과 순열을 푸는데 있어 모든 경우의 수를 알려주는 정말 유용한 라이브러리인 것 같다.