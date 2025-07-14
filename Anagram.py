# s1="anagram"
# s2="graaanm"
# if len(s1)!=len(s2):
#     print("not an anagram")
# else:
#     ans={}
#     for i in s1:
#         ans[i]=ans.get(i,0)+1
#     for j in s2:
#         if j in ans:
#             ans[j]-=1
#     freq=True
#     for i in ans.values():
#         if i!=0:
#             freq=False
#     if freq:
#         print("anagram")
#     else:
#         print("not an anagram")
        
        
str1="listen"
str2="silent"

if len(str1)!=len(str2):
    print("not anagram")
else:
    if sorted(str1)==sorted(str2):
       print("anagram")
    else:
       print("not anagram")


