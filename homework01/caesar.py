import typing as tp
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

def decrypt_caesar(ciphertext: str ="SBWKRQ  sbwkrq", shift: int = 3):
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
print("decrypted: ", decrypt_caesar()) 

def letter_converter(mode, input_char):
	abc123 = "abcdefghijklmnopqrstuvwxyz"
	
	# Letter to Code
	if mode == 1	: 
		found = abc123.find(input_char)
		if found > -1: return found
		else		 : return 23
		
	# Code to Letter
	elif mode == 2	: return abc123[int(input_char)]

###-----------------------------------------------------------------

def caesar_breaker_brute_force(cipher):
	plaintext = ''
	
	for key in range(1, 26):
		plaintext += '[' + str(key) + '] '
		for char in cipher:
			ascii_letter = letter_converter(1, char)
			ascii_letter = (ascii_letter + key) % 26
			plaintext += letter_converter(2, ascii_letter)
		plaintext += '\n'

	print(plaintext)

###-----------------------------------------------------------------

while True:
	cipher = input("Cipher: ").lower()
	caesar_breaker_brute_force(cipher)








