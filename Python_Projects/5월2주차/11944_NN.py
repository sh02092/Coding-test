import sys
input = sys.stdin.readline
n, m = map(str, input().split())
m=int(m)
for _ in range(int(n)):
    n += n    

if len(n)>m:
    print(n[:m])
else:
    print(n)