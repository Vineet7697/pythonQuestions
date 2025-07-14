s="hello world 123!"
vowel=0
consonant=0
for i in s:
    if  i in  "aeiou":
        vowel+=1
    elif i in "bcdfghjklmnpqrstvwxyz":
        consonant+=1
print("vowel:",vowel)
print("consonant:",consonant)