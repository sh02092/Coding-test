import numpy as np

a = np.array([1, 2, 3])
print(type(a), a.shape, a[0])

b = np.array([[1,2,3],[4,5,6]])
print(b)

a = np.zeros((2,2))
b = np.ones((1,2))
c = np.full((3,3), 0)
print(a)
print(b)
print(c)

d = np.eye(10)
print(d)
e = np.random.random((2,2))
print(e)

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
b = a[:2,1:3]
print(b)

print(a[0,1])
b[0,0] = 77
print(b)
print(a)
print(a[0,1])

a = np.array([[1,2],[3,4],[5,6]])
bool_idx = a>2
print(a)
print(bool_idx)
print(a[bool_idx])
print(a[a>2])

x = np.array([1,2])
y = np.array([1.0,2.0])
z = np.array([1,2], dtype=np.int64)
print(x.dtype, y.dtype, z.dtype)

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x+y)
print(np.add(x,y))
print(x-y)
print(np.subtract(x,y))
# 요소끼리의 곱
print(x*y)
print(np.multiply(x,y))
print(x/y)
print(np.divide(x,y))
print(x%y)
print(np.mod(x,y))
print(np.sqrt(x))

# 내적
print(np.dot(x,y))
print(x@y)
x = np.array([1,2])
y = np.array([3,4])
print(x@y)
print(x.dot(y))

x = np.array([[1,2],[3,4]])
# axis = 0 : 열의 합
# axis = 1 : 행의 합
print(x)
print(np.sum(x,axis=1))
print(np.sum(x, axis=0))
# x.T : transpose
print(x.T)


import matplotlib.pyplot as plt

# Sea bream data 도미 35마리 길이, 무게 data
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

# Smelt data 빙어 14마리 길이, 무게 data
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


# plt.scatter(bream_length, bream_weight)
# plt.scatter(smelt_length, smelt_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# Create the data of sea bream and smelt into a single list
# 도미 data 뒤에 빙어 data
# 도미 35마리, 빙어 14마리
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = [[l,w] for l, w in zip(fish_length, fish_weight)]
# 앞 35마리는 train data, 나머지 14마리는 test data
fish_target = [1]*35 + [0]*14

print(fish_data)
print(len(fish_data))

train_input = fish_data[:35]
train_target = fish_target[:35]

test_input = fish_data[35:]
test_target = fish_target[35:]

# 샘플링 편향(sampling bias) : Train data와 Test data가 섞여 있지 않아 한쪽으로 치우친 상황
print(train_target)
print(test_target)

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

# random.seed : numpy에서 일정한 결과를 얻기 위해 사용
np.random.seed(42)
# arange() 함수를 사용해 0~48까지 1씩 증가하는 배열 만듦
index = np.arange(49)
# shuffle() 함수를 사용해 배열을 무작위로 섞는다.
np.random.shuffle(index)

# 중요!!!!
# random하게 35 샘플을 training data로
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()