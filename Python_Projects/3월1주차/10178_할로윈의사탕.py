for _ in range(int(input())):
    a, b = map(int, input().split())
    you = a // b
    dad = a % b
    print("You get %d piece(s) and your dad gets %d piece(s)."%(you, dad))