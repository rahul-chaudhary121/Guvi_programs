s=input()
c=0
for i in range(len(s)):
    if s[i] in "0123456789":
        c+=1
print(c)