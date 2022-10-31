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
		return word[1:]+word[:1]
	
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
		self.key = key
		self.key_PBox = key_PBox
	
	
