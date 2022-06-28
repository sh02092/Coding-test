n = int(input())

for i in range(n):
    p = int(input())
    max = 0
    #name = ''
    for i in range(p):
        a, b = input().split()
        a = int(a)
        if max < a:
            max = a
            name = b

    print(name)
