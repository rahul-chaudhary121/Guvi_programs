#18
n,m=map(int,input().split())
for num in range(n+1,m):
    s=0
    x=num
    while(num>0):
        d=num%10
        s=s+d**3
        num=num//10
    if x==s:
        print(x,end=' ')