n=int(input())
ar=list(map(int,input().split()))
ar.sort()
if n%2!=0:
    print(ar[n//2])
else:
    print(ar[n//2-1],ar[n//2])