# Solving

## 쇠막대기
https://www.acmicpc.net/problem/10799
### 문제풀이
```python
fe = list(input())
stk = []
count = 0

for i in range(len(fe)):
    if fe[i] == '(':
        stk.append('(')
    else:
        if fe[i - 1] == '(':
            stk.pop()
            count += len(stk)
        else:
            stk.pop()
            count += 1
print(count)
```
'(' 일 때마다 stack에 넣어 ')'를 만날 경우 이전이 '('일 때와 ')' 일 때로 나눠 각각 stack을 pop 하고, '('일 때는 남은 stack 수만큼 count, ')'일 때는 1만큼 count한다.
### 의견
문제를 이해하기 까다로웠다. 또한 문제를 이해했음에도 접근법이 쉽지않아 고민을 만이 한 문제다.