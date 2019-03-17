# 22
n=int(input())
ar=list(map(int,input().split()))
m=ar[0]
for i in range(1,n):
    if ar[i]>m:
        m=ar[i]
print(m)