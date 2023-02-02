def pad(plaintext):
    """
    Pads the given plaintext with PKCS#7 padding to a multiple of 16 bytes.
    """
    padding_len = 16 - (len(plaintext) % 16)
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding

def unpad(plaintext):
    """
    Removes a PKCS#7 padding, returning the unpadded text and ensuring the
    padding was correct.
    """
    padding_len = plaintext[-1]
    assert padding_len > 0
    message, padding = plaintext[:-padding_len], plaintext[-padding_len:]
    assert all(p == padding_len for p in padding)
    return message

def xor(a, b):
    """
    Returns the bitwise XOR of the two given byte strings.
    """
    return bytes(x ^ y for x, y in zip(a, b))    

def cbc_encrypt(algo,key, iv, plaintext):
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ciphertext = b''
    prev = iv
    for block in blocks:
        prev = algo(xor(prev, block))
        ciphertext += prev
    return ciphertext

def cbc_decrypt(algo,key, iv, ciphertext):
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    plaintext = b''
    prev = iv
    for block in blocks:
        plaintext += xor(algo(block), prev)
        prev = block
    return unpad(plaintext)


def ctr_encrypt(algo, key, nonce, plaintext):
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ciphertext = b''
    counter = 0
    for block in blocks:
        keystream = algo(nonce + counter.to_bytes(8, 'little'))
        ciphertext += xor(block, keystream)
        counter += 1
    return ciphertext

def ctr_decrypt(algo, key, nonce, ciphertext):
    return ctr_encrypt(algo, key, nonce, ciphertext)

def ecb_encrypt(algo, key, plaintext):
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ciphertext = b''
    for block in blocks:
        ciphertext += algo(block)
    return ciphertext

def ecb_decrypt(algo, key, ciphertext):
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    plaintext = b''
    for block in blocks:
        plaintext += algo(block)
    return unpad(plaintext)

def ofb_encrypt(algo, key, iv, plaintext):
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ciphertext = b''
    prev = iv
    for block in blocks:
        prev = algo(prev)
        ciphertext += xor(block, prev)
    return ciphertext

def ofb_decrypt(algo, key, iv, ciphertext):
    return ofb_encrypt(algo, key, iv, ciphertext)

def cfb_encrypt(algo, key, iv, plaintext):
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ciphertext = b''
    prev = iv
    for block in blocks:
        prev = algo(prev)
        ciphertext += xor(block, prev)
    return ciphertext

def cfb_decrypt(algo, key, iv, ciphertext):
    return cfb_encrypt(algo, key, iv, ciphertext)

