n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
evenSum=0
oddSum=0
for i in range(n1,n2+1):
    if i%2==0:
        evenSum+=i
    else:
        oddSum+=i
print("Evensum=",evenSum)
print("oddsum=",oddSum)
