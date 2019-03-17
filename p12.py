s=input()
z=''
for i in range(len(s)-1,-1,-1):
    z+=s[i]
if s==z:
    print("yes")
else:
    print("no")