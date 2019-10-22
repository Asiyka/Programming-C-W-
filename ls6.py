plainText = input("Enter your text:")

cipherText = ""
for char in plainText:
    pos = ord(char)
    if 1<= pos<= 255:
        newpos = (pos-1+1)%10+1
    else:
        newpos = pos
    cipherText += chr(newpos)
print("Coded Message:",cipherText)
