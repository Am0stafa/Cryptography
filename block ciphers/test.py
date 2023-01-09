from AES import AES
iv = b'\xf2\xaf\xc1[\x125\x8d\xe8K\x8e\x16B\xd9t\x98F'
key = AES('Thats my Kung Fu Kung Fu')
c = key.encryptCBC('Two One Nine Two abdo mostafa', iv)
d = key.decryptCBC(c, iv)

print(c)
print(d)

