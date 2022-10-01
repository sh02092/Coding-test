# https://www.acmicpc.net/problem/1406
# 에디터- BJ_1406

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