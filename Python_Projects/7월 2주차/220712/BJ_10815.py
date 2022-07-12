n = int(input())
n_ = list(map(int, input().split()))
m = int(input())
m_ = list(map(int, input().split()))

n_ = sorted(n_)
m_count = [0 for _ in range(len(m_))]

for i in range(len(m_)):
    min = 0
    max = len(n_) - 1
    while min <= max:
        mid = (min + max) // 2
        if m_[i] == n_[mid]:
            m_count[i] += 1
            break
        elif m_[i] > n_[mid]:
            min = mid + 1
        elif m_[i] < n_[mid]:
            max = mid - 1

for i in range(len(m_count)):
    print(m_count[i], end=" ")
