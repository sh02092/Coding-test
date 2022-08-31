# Solving

## 이진 변환 반복하기
https://school.programmers.co.kr/learn/courses/30/lessons/70129
### 문제풀이
```python
def solution(s):
    answer = []
    count_0 = 0
    count = 0
    while s!='1':
        count_1 = 0 
        for i in s:
            if i == '1':
                count_1 += 1
            else:
                count_0 += 1
        s = ''
        while 1:
            if count_1 <= 1:
                break

            if count_1 % 2 == 0:
                s += '0'
            else:
                s += '1'
            count_1 //= 2
        s += str(count_1)
        count += 1
    
    answer.append(count)
    answer.append(count_0)

    return answer

s = "110010101001"
print(solution(s))
```
s가 1이 될 때까지 0을 지우고, 1의 개수를 새며 이진수를 만들기를 반복한다. 이 때, 이진수를 만드는 과정에서 순서를 거꾸로 입력한다. 예를들어 6을 이진수로 바꿀 때 '110'이 아닌'011'로 넣는다.
### 의견
어렵지 않은 문제였다.