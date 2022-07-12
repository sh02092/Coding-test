import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
m_count = [0 for _ in range(len(m_list))]

n_list = sorted(set(n_list))

for i in range(len(m_list)):
    min = 0
    max = len(n_list) - 1
    while min <= max:
        mid = (min + max) // 2
        if m_list[i] == n_list[mid]:
            m_count[i] += 1
            break
        elif m_list[i] > n_list[mid]:
            min = mid + 1
        elif m_list[i] < n_list[mid]:
            max = mid - 1

for i in m_count:
    print(i)