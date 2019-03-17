#26
def Merge_sort(arr,p,r):
    if p<r:
        q=(p+(r-1))//2
        Merge_sort(arr,p,q)
        Merge_sort(arr,q+1,r)
        Merge(arr,p,q,r)
def Merge(arr,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*n1
    R=[0]*n2
    for i in range(0,n1):
        L[i]=arr[p+i]
    for j in range(0,n2):
        R[j]=arr[q+1+j]
    i=0
    j=0
    k=p
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
        
        
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
n=int(input())
arr=list(map(int,input().split()))
Merge_sort(arr,0,n-1)
for i in range(0,n):
    print(arr[i],end=' ')