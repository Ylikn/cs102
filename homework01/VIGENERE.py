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
    text = plaintext
    key = keyword.lower()
    ciphertext = ""
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        viz = ord(text[i])
        gar = abc.find(key[i % len(key)])
        if (97 <= viz <= 122):
            if (97 <= viz + gar <= 122):
                ciphertext += chr(viz + gar)
            else:
                ciphertext += chr(viz + gar - 26)

        elif (65 <= viz <= 90):
            if (65 <= viz + gar <= 90):
                ciphertext += chr(viz + gar)
            else:
                ciphertext += chr(viz + gar - 26)
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
    text = str(ciphertext)
    key = str(keyword).lower()
    plaintext = ""
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        viz = ord(text[i])
        gar = abc.find(key[i % len(key)])
        if (97 <= viz <= 122):
            if (97 <= viz - gar <= 122):
                plaintext += chr(viz - gar)
            else:
                plaintext += chr(viz - gar + 26)

        elif (65 <= viz <= 90):
            if (65 <= viz - gar <= 90):
                plaintext += chr(viz - gar)
            else:
                plaintext += chr(viz - gar + 26)
        else:
            plaintext += text[i]

    return plaintext
