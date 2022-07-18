# Solving

## 괄호의 값- BJ_2504
https://www.acmicpc.net/problem/2504
### 문제풀이
```python
import sys
input = sys.stdin.readline

text = input().strip()
# ( : 2를 위한 스택
stack_2 = list()
# [ : 3을 위한 스택
stack_3 = list()
temp = 1
ans = 0
# 올바른 괄호 판별
paired = True

for i in range(len(text)):
    if text[i] == '(':
        stack_2.append(i)
        # '('가 있을 때마다 2를 곱하는 곱셈의 분배법칙
        temp *= 2
    elif text[i] == '[':
        stack_3.append(i)
        # '['가 있을 때마다 3을 곱하는 곱셈의 분배법칙
        temp *= 3
    elif text[i] == ')':
        if stack_2:
            # '()' 괄호가 완성되면 출력(ans)에 분배법칙으로 곱해진 값(temp) 더하기
            if text[i - 1] == '(':
                ans += temp
            stack_2.pop()
            # 2를 나누어 괄호 끝내기
            temp //= 2
        else:
            paired = False
            break
    elif text[i] == ']':
        if stack_3:
            # '[]' 괄호가 완성되면 출력(ans)에 분배법칙으로 곱해진 값(temp) 더하기
            if text[i - 1] == '[':
                ans += temp
            stack_3.pop()
            # 3을 나누어 괄호 끝내기
            temp //= 3
        else:
            paired = False
            break

if not stack_2 and not stack_3 and paired:
    print(ans)
else:
    print(0)

# 1. 스택에 넣어서 푼다는 생각을 못함
# 2. 묶음 처리(+, x)의 모든 경우의 수를 생각하다 쉽지 않다는 것을 느낌
```
입력에 대해 ( 또는 [ 가 있을 때마다 각각 2, 3씩 곱하고, 각 스택에 넣는다. ) 또는 ] 가 있을 때, 바로 앞 원소가 각각 ( 또는 [ 일 경우 출력에 분배법칙으로 곱해진 값(temp)의 값을 더한다. 이후 괄호가 완성됐으므로 스택에서 마지막에 쌓인 괄호를 없앤다. 과정에서 올바른 괄호가 판별된다면 올바른 출력, 판별되지 않는다면 0 출력

### 의견
(), []와 같이 괄호가 붙어있는 부분을 2, 3으로 치환하여 풀어가는 방식을 생각했다. 하지만 전체 괄호를 처리하는데 있어서 묶음 처리(+, x)의 모든 경우의 수를 생각하는 것이 쉽지 않았다. 따라서 구글링을 하게 되었는데 스택, 곱셈의 분배법칙을 활용하면 어렵지 않은 코딩으로 문제를 풀 수 있었다. (, [ 각각의 스택을 만들어 놓고, (, [ 이 나올 때마다 각각의 스택에 저장하여 ), ]이 나오면 스택을 가장 마지막에 쌓은 것부터 없애며 짝이 맞으면 출력에 더하고, 아니면 2, 3으로 나누는 방식을 사용했다. 문제 푸는 방법을 알고 보니 이해하는데 어려움은 없었지만, 다시 풀어보려 한다면 생각하기 어려울 것 같은 문제였다.