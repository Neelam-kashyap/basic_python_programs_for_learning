a=int(input())
c=0
b=[]
while(True):
    a=a+1
    for x in range(1,a+1):
        if a%x==0:
            c=c+1
        if c==2:
            b.append(a)
        if len(b)==10:
            break
print(b)
