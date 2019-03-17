s=input()
flag=True
for i in range(len(s)):
    if s[i] not in "0123456789.":
        flag=False
        break
if flag==True:
    print("Yes")
else:
    print("No")