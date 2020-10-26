a=int(input('number: '))
c=0
for num in range(1,a + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
    else:
        print(a)
