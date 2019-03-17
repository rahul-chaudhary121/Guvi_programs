n=int(input())
ar=list(map(int,input().split()))
s=0
for i in range(n):
    s+=ar[i]
print(s//n)