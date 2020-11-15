def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    letters_Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_Lowercase = "abcdefghijklmnopqrstuvwxyz"
    a = 26

    while len(keyword) < len(plaintext):
        keyword += keyword

    ciphertext = ""
    for i in range(len(plaintext)):
        location = ord(plaintext[i])

        if keyword[i] in letters_Uppercase:
            Newlocation = ord(keyword[i]) - ord("A")
        elif keyword[i] in letters_Lowercase:
            Newlocation = ord(keyword[i]) - ord("a")

        if (97 <= location + Newlocation <= 122) and location > 96 and location < 123 \
                or (65 <= location + Newlocation <= 90) and location > 64 and location < 91:
            ciphertext += chr(location + Newlocation)
        else:
            ciphertext += chr(location + Newlocation - a)

    return ciphertext




def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    letters_Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_Lowercase = "abcdefghijklmnopqrstuvwxyz"
    a = 26

    while len(keyword) < len(ciphertext):
        keyword += keyword

    plaintext = ""

    for i in range(len(ciphertext)):
        location = ord(ciphertext[i])

        if keyword[i] in letters_Uppercase:
            Newlocation = ord(keyword[i]) - ord("A")
        elif keyword[i] in letters_Lowercase:
            Newlocation = ord(keyword[i]) - ord("a")

        if (97 <= location - Newlocation <= 122) and location > 96 and location < 123 \
                or (65 <= location - Newlocation <= 90) and location > 64 and location < 91:
            plaintext += chr(location - Newlocation)
        else:
            plaintext += chr(location - Newlocation + a)
    return plaintext
