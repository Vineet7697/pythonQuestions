# s="hello"

# ans={}
# for i in s:
#     # if i in ans:
#     #     ans[i]=ans.get(i)+1
#     # else:
#     #     ans[i]=1
    
#         ans[i]=ans.get(i,0)+1
# print(ans)
        
    
    
#using function
def Count_frequency(n):
    ans={}
    for i in n:
        ans[i]=ans.get(i,0)+1
    return ans
s="hello"
print(Count_frequency(s))