num=int(input("enter the number:"))
a=0
b=1
print(a,b,end=" ")
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    
    
#using function
def fibonacci(n,a=0,b=1):
    if n==0:
        print(a)
    elif n==1:
        print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
    print(c)
    
n=8
fibonacci(n)