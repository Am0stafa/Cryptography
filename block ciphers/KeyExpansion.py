import numpy as np


class AES_KeyExpansion:
	def __init__(self,sbox,Rcon,key):
		self.key = self.formatKey(key)
		self.sbox = sbox
		self.Rcon = Rcon
		self.options = {
			'wordLength':{
				128:4,
				192:6,
				256:8
			},
			'words':{
				128:44,
				192:78,
				256:112
			},
			'numberOfKeys':{
				128:11,
				192:13,
				256:15
			}
		}
	
	#! function to convert string to hex
	def str2hex(self,message):
		return ''.join(format(ord(i), '02x') for i in message)
	
	#! formate the hex into an array of 4 bytes
	def hex2array(self,hex):
		return [hex[i:i+2] for i in range(0, len(hex), 2)]
		
	#! formate the user input
	def formatKey(self,key):
		return self.hex2array(self.str2hex(str(key)))
	
	def hex2binary(self,hex):
		return bin(int(str(hex), base = 16))
	
	def decimalToBinary(self,n):
		return bin(n).replace("0b", "")
		
	def binaryToDecimal(self,n):
		return int(n,2)
	
	def str2bin(self,message):
		return ''.join(format(ord(i), '08b') for i in message)
	
	def xORtwoBits(self,a,b):
		y=int(a,2) ^ int(b,2)
		return y   
	
	#! first convert to binary then xor then convert back to hex and return it
	def heXor(self,hex1, hex2):
		bin1 = self.hex2binary(hex1)
		bin2 = self.hex2binary(hex2)
		
		xord = self.xORtwoBits(bin1,bin2)
		
		#^ remove 0x
		hexed = hex(xord)[2:]
		
		if len(hexed) != 8:
			hexed = '0' + hexed
			
		return hexed
		
	def returnKeys(self,words):
		keys=[[]]*11
		for i in range(len(words)):
			if i % 4 == 0:
				keys[int(i/4)] = words[i:i+4]	
		return keys
		
	def shift4Bits(self,word):
		return word[1:] + word[:1]
	
	def shift8Bits(self,word):
		return word[2:]+word[:2]

	def shift16Bits(self,word):
		return word[4:]+word[:4]

	def getSbox(self,byte):
		a = byte[0]
		b = byte[1]
		
		if not a.isdigit():
			a = ord(a)-87
		if not b.isdigit():
			b = ord(b)-87
		
		return (hex(self.sbox[int(a)][int(b)])[2:])



	def keyExpansion(self):
		words = [[]]*44
		
		#^ first 4 words are the key
		for i in range(0,len(self.key),4):
			words[i//4]=self.key[i:i+4]
		
		for i in range(4, 44):
			#* equivalent to k[n-1]:w[i] OR k[n-1]:w[i] 
			wordAtI = words[i-4]
			#* equivalent to k[n]:w[i-1] OR k[n-1]:w[i-1]
			wordAtN_1 = words[i-1] #& this must change if we are at w0

			if i % 4 == 0:
				if i == 20:
						print(wordAtN_1)
				#^ rotate the word
				wordAtN_1 = self.shift4Bits(wordAtN_1)
				
				afterSbox = []
				
				for j in wordAtN_1:
					afterSbox.append(self.getSbox(j))
					
				rcon =  hex(self.Rcon[int(i/4)])[2:]
				strSBox = ''.join(afterSbox)
							
					
				wordAtN_1 = self.heXor(strSBox,rcon)
				
				

			wordAtI = ''.join(wordAtI)
			wordAtN_1 = ''.join(wordAtN_1)
			
			finalXor = self.heXor(wordAtI,wordAtN_1)
			words[i] = [finalXor[:2], finalXor[2:4], finalXor[4:6], finalXor[6:8]]
			
		return self.returnKeys(words)

class DES_KeyExpansion:
	def __init__(self,key,key_PBox):
		self.key = self.formateKey(key)
		self.key_PBox = key_PBox
	
	def formateKey(self,key):
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