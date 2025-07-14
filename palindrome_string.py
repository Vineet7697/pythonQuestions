string=input("enter the string:")
reverse=""
for i in string:
    reverse=i+reverse
if string==reverse:
    print("palindrme")
else:
    print("not palindrome")