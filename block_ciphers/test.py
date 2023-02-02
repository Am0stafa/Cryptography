from AES import AES
iv = b'\xf2\xaf\xc1[\x125\x8d\xe8K\x8e\x16B\xd9t\x98F'
key = AES('Thats my Kung panda')
# c = key.encryptCBC('Two One Nine Two abdo mostafa',iv)
# d = key.decryptCBC(c, iv)

c = key.encryptECB('Two One Nine Two abdo mostafa')
d = key.decryptECB(c)

# c = key.encryptCTR('Two One Nine Two abdo mostafa',iv)
# d = key.decryptCTR(c, iv)

# c = key.encryptOFB('Two One Nine Two abdo mostafa',iv)
# d = key.decryptOFB(c, iv)

# c = key.encryptCFB('Two One Nine Two abdo mostafa',iv)
# d = key.decryptCFB(c, iv)


print(c)
print(d)

