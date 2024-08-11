#defining caesar cipher

def encrypt(plaintext,n):
    cipher = ""

    for i in range(len(plaintext)):
        ch = plaintext[i]

        if ch==" ":
            cipher+=" "
        
        elif (ch.isupper()):
            cipher += chr((ord(ch) + n-65 ) % 26 + 65)
        
        else:
            cipher += chr((ord(ch) + n-97 ) % 26 + 97)
    
    return cipher

text = "i am best "
n = 1

print("encrypted fomat :" + encrypt(text,n))
