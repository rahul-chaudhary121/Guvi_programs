num=int(input())
while(1):
    if num%2==0:
        num=num//2
        if num==1:
            print("yes")
            break
    else:
        print("no")
        break