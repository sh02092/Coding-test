import numpy as np
import matplotlib.pyplot as plt

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# list로 만들기
fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]
print(fish_data)

# numpy 함수인 column_stack() : 전달받은 리스트를 일렬로 세운 다음 차례대로 나란히 연결
fish_data = np.column_stack((fish_length, fish_weight))
print(fish_data.shape)

# concatenate() : 두 개의 배열 연결
fish_target = np.concatenate((np.ones(35), np.zeros(14)))

# 아래 방법은 번거롭다.. 귀찮다...??
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

np.random.seed(42)
index = np.arange(49)
np.random.shuffle(index)

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

# 간편한 방법
# train_test_split() : 전달되는 리스트나 배열을 비율에 맞게 train, test data로 나눠준다. 알아서 섞어주기도 한다.
from sklearn.model_selection import train_test_split
# 처음 두개는 input data, 뒤 두개는 target data
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state = 42) # 이게 끝...??

print(train_input.shape, test_input.shape)
print(train_target.shape, test_target.shape)

# 샘플링 편향 나타남.. 
print(train_target, test_target)

# 만능이야..
# train_test_split() 함수의 stratify parameter에 target data를 전달하면, 비율에 맞게 데이터를 나눈다...
# 미쳤네

train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, stratify = fish_target, random_state = 42)

# 비율 맞았다... 도랐네.....
print(train_target, test_target)

from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()

kn.fit(train_input, train_target)
kn.score(test_input, test_target)
