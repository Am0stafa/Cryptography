from AES import AES

key = AES(b'Thats my Kung Fu Kung Fu')
c = key.encrypt_block(b'Two One Nine Two')
d = key.decrypt_block(c)
# print(d)