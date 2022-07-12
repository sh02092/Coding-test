from collections import deque
import sys
input = sys.stdin.readline

n_ = deque()
for _ in range(int(input())):
    text = input().rstrip()
    if text[0] == 'p':
        if text[1] == 'u':
            n_.append(int(text[5:]))
        elif text[1] == 'o':
            if n_:
                print(n_[-1])
                n_.pop()
            else:
                print(-1)

    elif text[0] == 't':
        if n_:
            print(n_[-1])
        else:
            print(-1)
    elif text[0] == 's':
        print(len(n_))
    elif text[0] == 'e':
        if n_:
            print(0)
        else:
            print(1)