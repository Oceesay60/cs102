import string
import typing as tp



def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.


    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for x in plaintext:
        if x != " ":
            value = string.ascii_uppercase.find(x)
            if value == -1:
                value = string.ascii_lowercase.find(x)
                if value == -1:
                    ciphertext += x
                else:
                    location = (value + shift) % len(string.ascii_lowercase)
                    ciphertext += string.ascii_lowercase[location]
            else:
                location = (value + shift) % len(string.ascii_uppercase)
                ciphertext += string.ascii_uppercase[location]
        else:
            ciphertext += " "
    return ciphertext
 



def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:

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
    plaintext = ""
    for x in ciphertext:
        if x != " ":
            value = string.ascii_uppercase.find(x)
            if value == -1:
                value = string.ascii_lowercase.find(x)
                if value == -1:
                    plaintext += x
                else:
                    location = (value - shift) % len(string.ascii_lowercase)
                    plaintext += string.ascii_lowercase[location]
            else:
                location = (value - shift) % len(string.ascii_uppercase)
                plaintext += string.ascii_uppercase[location]
        else:
            plaintext += " "
    return plaintext 


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






