def encrypt_caesar(plaintext, shift):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    alp = 26
    sp = shift % 26
    for i in range(len(text)):
        char = text[i]
        if not ((97 <= ord(char) <= 122) or (65 <= ord(char) <= 90)):
            ciphertext += char
            continue
        if (97 <= ord(char) + sp <= 122) or (65 <= ord(char) + sp <= 90):
            ciphertext += chr(ord(char) + sp)
        else:
            ciphertext += chr(ord(char) - alp + sp)
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    alp = 26
    sp = shift % 26
    for i in range(len(text)):
        char = text[i]
        if not ((97 <= ord(char) <= 122) or (65 <= ord(char) <= 90)):
            plaintext += char
            continue
        if (97 <= ord(char)-sp <= 122) or (65 <= ord(char)-sp <= 90):
            plaintext += chr(ord(char)-sp)
        else:
            plaintext += chr(ord(char)+alp-sp)
    return plaintext
