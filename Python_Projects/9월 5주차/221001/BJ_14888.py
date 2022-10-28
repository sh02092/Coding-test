def solution(answers):
    answer = []
    fir = [1,2,3,4,5]
    sec = [2,1,2,3,2,4,2,5]
    thi = [3,3,1,1,2,2,4,4,5,5]
    cnt_fir = 0
    cnt_sec = 0
    cnt_thi = 0
    for i in range(1, len(answers) + 1):
        if answer[i - 1] == fir[(i) % 5]:
            cnt_fir += 1
        if answer[i - 1] == sec[(i) % 8]:
            cnt_sec += 1
        if answer[i - 1] == thi[(i) % 10]:
            cnt_thi += 1
    cnt = [[1, cnt_fir], [2, cnt_sec], [3, cnt_thi]]
    print(cnt)
    cnt.sort(key = lambda x: x[1])
    print(cnt)
    return answer


print(solution([1,2,3,4,5]))