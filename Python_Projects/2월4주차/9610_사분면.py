n = int(input())

q_1=0
q_2=0
q_3=0
q_4=0
axis=0

for i in range(n):
    x, y = map(int, input().split())
    if x==0 or y==0:
        axis+=1
    elif x>0 and y>0:
        q_1+=1
    elif x<0 and y>0:
        q_2+=1
    elif x<0 and y<0:
        q_3+=1
    elif x>0 and y<0:
        q_4+=1

print("Q1: %s"%q_1)
print("Q2: %s"%q_2)
print("Q3: %s"%q_3)
print("Q4: %s"%q_4)
print("AXIS: %s"%axis)
