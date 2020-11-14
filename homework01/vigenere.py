


def encrypt_vigenere(plaintext, keyword):
    alpha_b= "abcdefghijklmnopqrstuvwxyz "

    letter_to_index = dict(zip(alpha_b, range(len(alpha_b))))
    index_to_letter = dict(zip(range(len(alpha_b)), alpha_b))

    ciphertext = ""
    split_plaintext = [
        plaintext[i : i + len(keyword)] for i in range(0, len(plaintext), len(keyword))
    ]

    for each_split in split_plaintext:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[keyword[i]]) % len(alpha_b)
            ciphertext += index_to_letter[number]
            i += 1

    return ciphertext


def decrypt(ciphertext, keyword):
    alpha_C= "abcdefghijklmnopqrstuvwxyz "

    letter_to_index = dict(zip(alpha_C, range(len(alpha_C))))
    index_to_letter = dict(zip(range(len(alpha_C)), alpha_C))

    plaintext = ""
    split_encrypted = [
        ciphertext[i : i + len(keyword)] for i in range(0, len(ciphertext), len(keyword))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[keyword[i]]) % len(alpha_C)
            plaintext += index_to_letter[number]
            i += 1

    return plaintext


def main():
    plaintext = "python"
    keyword = "banana"
    encrypted_message = encrypt_vigenere(plaintext, keyword)
    decrypted_message = decrypt(encrypted_message, keyword)

    print("Original message: " + plaintext)
    print("Encrypted message: " + encrypted_message)
    print("Decrypted message: " + decrypted_message)


main()