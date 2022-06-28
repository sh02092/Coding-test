test = int(input())

for i in range(test):
    num = int(input())
    univ = {}
    for i in range(num):
        a, b = input().split()
        univ[a]=int(b)
    swap_univ = dict(zip(univ.values(), univ.keys()))
    print(swap_univ[max(swap_univ)])