student=[]
total=0
for i in range(5):
    a=int(input())
    if a<40:
        a=40
    total+=a

total/=5
total=int(total)
print(total)
