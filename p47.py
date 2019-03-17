#47
n=int(input())
ar=list(map(int,input().split()))
s=l=ar[0]
for i in range(1,n):
    if s>ar[i]:
        s=ar[i]
    if l<ar[i]:
        l=ar[i]
print(s,l)