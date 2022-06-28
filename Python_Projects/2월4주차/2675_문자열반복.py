cases = int(input())

for i in range(cases):
    r, s = input().split()
    r=int(r)
    s=str(s)
    text=''
    for j in s:
        text += j*r
    print(text)