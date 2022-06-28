num = int(input())

num_1=0
num_0=0
for i in range(num):
    temp = int(input())
    if temp==1:
        num_1+=1
    else:
        num_0+=1

if num_1 > num_0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
