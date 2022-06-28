cases = int(input())

for i in range(cases):
    test = list(map(str, input().split()))
    answer = float(test[0])
    for j in range(1, len(test)):
        if test[j] == "@":
            answer *= 3
        elif test[j] == "%":
            answer += 5
        elif test[j] == "#":
            answer -= 7

    print("%0.2f" % answer)