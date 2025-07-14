li=[1,2,3,4,2,4,2,3]
list=[]
for i in li:
    ans=False
    for j in list:
        if i==j:
            ans=True
    if not ans:
        list.append(i)
print(list)

# for i in range(len(li)):
#     for j in range(i+1,(len(li))):
#         if li[i]>li[j]:
#             li[i],li[j]=li[j],li[i]
# print(li)
# for i in range(len(li)):
#     if i==0 or li[i]!=li[i-1]:
#         list.append(li[i])
# print(list)