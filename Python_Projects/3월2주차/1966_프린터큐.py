for _ in range(int(input())):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    
    # index 배열을 따로 만들어 m 번째를 1로
    q_index = [[0] for _ in range(n)]
    q_index[m] = 1

    count = 0
    while 1:
        if q[0] == max(q):
            count += 1
            if q_index[0] == 1:
                print(count)
                break
            else:
                del q_index[0]
                del q[0]
        else:
            q.append(q[0])
            q_index.append(q_index[0])
            del q[0]
            del q_index[0]
