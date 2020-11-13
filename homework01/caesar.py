#c=(x-n)%26

def encriypt_caesar(plaintext: str = "python3.6 PYTHON python" , shift: int = 3):
    ciphertext = ""
    for char in plaintext:
        if char ==" ":
             ciphertext=ciphertext+char
        elif char.isupper():
             ciphertext=ciphertext+chr((ord(char)+shift-65)%26+65)
        else:
            ciphertext=ciphertext+chr((ord(char)+shift-97)%26+97)
    return ciphertext
print(" encripted:", encriypt_caesar())

def decrypt_caesar(ciphertext: str ="SBWKRQ  sbwkrq  Sbwkrq3.6", shift: int = 3):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    #alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""
    for char in ciphertext:
        if char ==" ":
             plaintext=plaintext+char
        elif char.isupper():
           plaintext=plaintext+chr((ord(char)-shift-65)%26+65)
        else:
             plaintext=plaintext+chr((ord(char)-shift-97)%26+97)
    return plaintext 
print("decrypted:", decrypt_caesar()) 









