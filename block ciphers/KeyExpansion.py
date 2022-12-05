import numpy as np


class AES_KeyExpansion:
	def __init__(self, sbox, Rcon, key):
		pass
		
		
		
class DES_KeyExpansion:
	def __init__(self, key, key_PBox):
		self.key = self.formateKey(key)
		self.key_PBox = key_PBox

	def formateKey(self, key):
		binaryKey = self.toBinary(key)
		strKey = "".join(binaryKey)
		if len(strKey) > 56:
	        strKey = strKey[:56]
	    if len(strKey) < 56:
	        strKey = strKey + "0"*(56-len(strKey))
	    keys = []
	    for i in strKey:
	        keys.append(i)
	    return keys 
	
	def toBinary(self,a):
	  l,m=[],[]
	  for i in a:
	    l.append(ord(i))
	  for i in l:
	    m.append(str(int(bin(i)[2:])))
	  return m
	  
	def keypermute(self,key16):
	    keypermuted = np.empty([16,48])
	    l = 0
	    for k in key16:
	        j = 0
	        for i in self.key_PBox:
	            keypermuted[l][j] = k[i - 1]
	            j += 1
	        l += 1
	    return keypermuted
	    
	def keyshift(self,toshift,n):
	    if (n == 1) or (n == 2) or (n == 9) or (n == 16):
	        toshift= np.roll(toshift,-1)
	        return toshift
	    else:
	        toshift = np.roll(toshift, -2)
	        return toshift
	def keyschedule(self):
	    left = self.key[0:28]
	    right = self.key[28:56]
	    shifted = np.zeros(56)
	    key16 = np.zeros([16,56])
	    for i in range(1,17):
	        shifted[0:28] = self.keyshift(left,i)
	        shifted[28:56] = self.keyshift(right,i)
	        left = shifted[0:28]
	        right = shifted[28:56]
	    #add shifted to key16 and return key16
	        key16[i - 1] = shifted
	    #key16 is the final shifted 16 key pair now to permute
	    key16 = self.keypermute(key16)
	    key16 = [list(map(int, x)) for x in key16]
	    key16 = np.array(key16)
	    #convert numpy array into array
	    keyMet = [list(map(int, key)) for key in key16]
	    for i in range(0,16):
	        keyMet[i] = "".join(map(str, keyMet[i]))
	    
	    return keyMet