# Solving

## 2개 이하로 다른 비트
https://school.programmers.co.kr/learn/courses/30/lessons/77885
### 문제풀이
```python
def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)
            continue
        
        # 10진수 2진수로 변환하여 list에 1개씩 입력
        temp = list('0' + bin(i)[2:])
        # 오른쪽부터 '0' 찾기
        idx = ''.join(temp).rfind('0')
        # 찾은 '0'의 값을 '1'로 바꿈
        temp[idx] = '1'
        # 다음 index의 값을 '0'으로 바꿈
        temp[idx + 1] = '0'
        # 2진수를 10진수로 변경
        answer.append(int(''.join(temp), 2))

    return answer
```
짝수인 경우 1 더하여 answer list에 입력한다.
홀수인 경우 10진수를 2진수로 변경하고, 자릿수가 바뀔 것을 고려하여 맨 앞에 '0'을 추가한다. 이후 오른쪽에서부터 가장 가까운 '0'을 찾아 '1'로 바꾸고, 다음 index 값을 '0'으로 바꾼다. 다시 10진수로 바꾸고 answer list에 입력한다.
### 의견
문제의 제한 사항에 numbers의 모든 수의 값이 10^15까지인 것을 봤을 때 시간 초과가 나는 문제인 것은 알고 있었지만.. 결국 혼자 시간 초과의 문제를 해결할 수는 없었다. 찾아보니 홀수의 경우 규칙이 있는 것을 알았고, 알고난 후 어렵지 않게 해결할 수 있었다.