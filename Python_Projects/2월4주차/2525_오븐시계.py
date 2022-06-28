a,b=input().split()
a=int(a)
b=int(b)
c=input()
c=int(c)

if b+(c%60)>=60:
    a_c=int(c/60)+1
    b_c=b+(c%60)-60

else :
    a_c=int(c/60)
    b_c=b+(c%60)

temp=a+a_c

if temp>=24:
    temp-=24


print("%s %s"%(temp, b_c))

