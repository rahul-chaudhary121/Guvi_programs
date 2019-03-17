ar=list(map(int,input().split()))
s=ar[0]
for i in range(1,len(ar)):
    if s>ar[i]:
        s=ar[i]
print(s)