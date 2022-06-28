for j in range(int(input())):
    li = list(map(int, input().split()))
    li.pop(0)
    li = sorted(li)

    gap = []
    for i in range(1, len(li)):
        gap.append(li[i] - li[i - 1])
    
    print('Class %d' % (j + 1))
    print('Max %d, Min %d, Largest gap %d' % (li[-1], li[0], max(gap)))
