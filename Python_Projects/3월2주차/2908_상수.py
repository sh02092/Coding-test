a, b = map(int, input().split())

rev_a = int(str(a)[::-1])
rev_b = int(str(b)[::-1])

if rev_a > rev_b:
    print(rev_a)
else:
    print(rev_b)