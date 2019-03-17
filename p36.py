s=input()
c=0
for i in range(len(s)):
    if s[i] in "./~`!@#$%^&*)(_-=+|\*<>:;}{":
        c+=1
print(c)