num=int(input("enter the number:"))
a=0
b=1
print(a,b,end=" ")
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
  
    