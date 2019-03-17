s=input()
if len(s)==1:
    if (ord(s)>=65 and ord(s)<=92) or (ord(s)>=97 and ord(s)<=122):
        print("Alphabet")
else:
    print("No")