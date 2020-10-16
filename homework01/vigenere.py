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
    alpha_B = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext= []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            mj = alpha_B.index(ch)
            kj = alpha_B.index(key[(index - space) % len(key)])
            cj = (mj + kj) % len(alpha_B)
            ciphertext.append(alpha_B[cj])
        else:
            space += 1
            ciphertext.append(' ')
    return ''.join(ciphertext)
  
def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            cj = alpha_B.index(ch)
            kj = alpha_B.index(key[(index - space) % len(key)])
            mj = (cj - kj) % len(alpha_B)
            result.append(alpha_B[mj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)
  
print(encrypt_vigenere('klic', 'tajnytext'))                 
print(encrypt_vigenere('klic', 'tajny text s mezerama'))       
print(encrypt_vigenere('dlouhyklic', 'mega zasifrovany text'))  
  
print(decrypt_vigenere('klic', 'dlrpiemzd'))                   
print(decrypt_vigenere('klic', 'dlrpi emzd d ugjpzcwl'))        
print(decrypt_vigenere('dlouhyklic', 'ppuu gyctntrgohf roib'))  
