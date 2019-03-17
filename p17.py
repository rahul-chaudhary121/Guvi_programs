num=int(input())
s=0
x=num
while(num>0):
    d=num%10
    s=s+d**3
    num=num//10
if x==s:
    print("yes")
else:
    print("no")
    