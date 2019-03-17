s=input()
l=['0','1','2','3','4','5','6','7','8','9']
c=d=0
for i in s:
    if (i>='A' and i<='Z') or (i>='a' and i<='z'):
        c+=1
    elif i in l:
        d+=1
if c>0 and d>0:
    print("yes")
else:
    print("no")