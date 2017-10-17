def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        codef = ord(text[i])
        codes = abc.find(key[i % len(key)])
        if (97 <= codef <= 122):
            if (97 <= codef + codes <= 122):
                ciphertext += chr(codef + codes)
            else:
                ciphertext += chr(codef + codes - 26)

        elif (65 <= codef <= 90):
            if (65 <= codef + codes <= 90):
                ciphertext += chr(codef + codes)
            else:
                ciphertext += chr(codef + codes - 26)
        else:
            ciphertext += text[i]
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        codef = ord(text[i])
        codes = abc.find(key[i % len(key)])
        if (97 <= codef <= 122):
            if (97 <= codef - codes <= 122):
                plaintext += chr(codef - codes)
            else:
                plaintext += chr(codef - codes + 26)

        elif (65 <= codef <= 90):
            if (65 <= codef - codes <= 90):
                plaintext += chr(codef - codes)
            else:
                plaintext += chr(codef - codes + 26)
        else:
            plaintext += text[i]
    return plaintext
    