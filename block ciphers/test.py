from AES import AES

key = AES('Thats my Kung Fu Kung Fu')
c = key.encrypt_block('Two One Nine Two')
d = key.decrypt_block(c)
# print(d)

