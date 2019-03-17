s=input()
flag=True
for i in s:
    if i not in "01":
        flag=False
        break
if flag==True:
    print("yes")
else:
    print("no")