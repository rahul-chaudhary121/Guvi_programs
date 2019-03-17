s=input()
if s in "aeiou" or s in "AEIOU":
    print("Vowel")
elif s in "!@#$%^&*(/-_+.,":
    print("invalid")
else:
    print("Consonant")