# from DES import DES

# des = DES('abdomostafa',"cbc")
# # print()
# print(des.Decrypt(des.Encrypt("0000000100100011010001010110011110001001101010111100110111101111")))


import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..' )
sys.path.append( mymodule_dir )




from AES import AES

AES('Thats my Kung Fu', 'v').encryptedMsg('Two One Nine Two')


# [['61', '16', '62', '26'], ['64', '46', '6f', 'f6'], ['6d', 'd6', '6f', 'f7'], ['73', '33', '36', '66']]
# [['61', '62', '64', '6f'], ['4d', '6f', '73', '74'], ['61', '66', '61', '47'], ['61', '6e', '6e', '61']]
    

    
