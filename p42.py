#42
s1,s2=map(str,input().split())
i=j=0
if len(s1)>len(s2):
    print(s1)
elif len(s2)>len(s1):
    print(s2)
else:
    while(i<len(s1) and j<len(s2)):
        if s1[i]>s2[j]:
            print(s1)
            break
        elif s1[i]<s2[j]:
            print(s2)
            break
        i+=1
        j+=1

    