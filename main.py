from art import *
from classical_ciphers.classicalCiphers import ClassicalCiphers
from block_ciphers.AES import AES
from block_ciphers.DES import DES
from asymmetric_ciphers.RSA import runRSA
from asymmetric_ciphers.diffieHellman import runDH
from elliptic_curves.elliptic_curve import EllipticCurve
from elliptic_curves.ECDH import runECDH
from secret_sharing.SSS import SSS


art_1=text2art("Abdo crypto module")
print(art_1)
iv = b'\xf2\xaf\xc1[\x125\x8d\xe8K\x8e\x16B\xd9t\x98F'
key = AES('Thats my Kung panda')
c = key.encryptCBC('Two One Nine Two abdo mostafa', iv)
d = key.decryptCBC(c, iv)

print(c)
print(d)

