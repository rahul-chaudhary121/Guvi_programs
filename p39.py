ar=list(map(int,input().split()))
m=ar[0]
for i in range(1,len(ar)):
    if m<ar[i]:
        m=ar[i]
print(m)