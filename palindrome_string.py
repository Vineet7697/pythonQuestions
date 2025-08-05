string=input("enter the string:").lower()
reverse=""
for i in string:
    reverse=i+reverse
if string==reverse:
    print("palindrme")
else:
    print("not palindrome")






#using function
def is_palindrome(s):
    st=0 
    end=len(s)-1
    
    while(st<end):
        if not s[st].isalnum():  #inbuilt functoin isalnum() isalpha()  isdigit()
            st+=1
            continue
        if not s[end].isalnum():  #inbuilt functoin isalnum() isalpha()  isdigit()
            end-=1 
            continue
        if s[st].lower()!=s[end].lower():
            return "not palindorme"
        st+=1
        end-=1
    return "palindrome"
    

str="Ac3?e3c&a"
print(is_palindrome(str))
