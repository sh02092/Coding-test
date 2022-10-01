# Solving

## 에디터
https://www.acmicpc.net/problem/1406
### 문제풀이
```python
import sys
input = sys.stdin.readline

letter = list(input().rstrip())
let_stk = list()

for _ in range(int(input())):
    ord = input().split()

    if ord[0] == 'L':
        if letter:
            let_stk.append(letter.pop())
    elif ord[0] == 'D':
        if let_stk:
            letter.append(let_stk.pop())
    elif ord[0] == 'B':
        if letter:
            letter.pop()
    else:
        letter.append(ord[1])

letter += reversed(let_stk)
print(''.join(letter))
```
커서를 기준으로 좌측, 우측을 각각 스택으로 만든다. 명령어에 따라 진행하고, 마지막에 우측 스택을 뒤집어 붙인다. 문자열 출력은 join을 사용해 하나의 string으로 출력한다.
### 의견
코테가 많이 부족하다... .join(), rstrip(), 스택 사용법... 등등...