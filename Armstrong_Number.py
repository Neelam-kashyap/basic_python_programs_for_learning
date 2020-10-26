def le(n):
    c=0
    while(n>0):
        n =int(n/10)
        c=c+1
    return c

def armstrong(n):
    f=n
    a=le(n)
    d=0
    while(n>0):
        b=int(n%10)
        n=int(n/10)
        d= d + (b**a)
    if d==f:
        print(d)

n=int(input())
for x in range(n+1):
    armstrong(x)
input()
