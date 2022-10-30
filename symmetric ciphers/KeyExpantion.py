class AES_KeyExpansion:
    def __init__(self,sbox,Rcon,key):
        self.key = formatKey(key)
        self.sbox = sbox
        self.Rcon = Rcon
        self.options = {
            wordLength:{
                128:4,
                192:6,
                256:8
            },
            words:{
                128:44,
                192:78,
                256:112
            },
            numberOfKeys:{
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
    	return hex2array(str2hex(str(key)))
    
    def hex2binary(self,hex):
	    return bin(int(str(hex), 16))
    
    def decimalToBinary(self,n):
        return bin(n).replace("0b", "")
        
    def binaryToDecimal(self,n):
        return int(n,2)
    
    def str2bin(message):
	    return ''.join(format(ord(i), '08b') for i in message)
    
    def xORtwoBits(self,a,b):
        y=int(a,2) ^ int(b,2)
        return y   
    
    def heXor(self,hex1, hex2):
    	#! first convert to binary then xor then convert back to hex and return it
    	
    	bin1 = hex2binary(hex1)
    	bin2 = hex2binary(hex2)
    	
    	xord = int(bin1, 2) ^ int(bin2, 2)
    	
    	#^ remove 0x
    	hexed = hex(xord)[2:]
    	
    	if len(hexed) != 8:
    		hexed = '0' + hexed
    		
    	return hexed
    	
    def returnKeys(self,words):
        keys=[[]]*11
        for i in range(len(w)):
            if i % 4 == 0:
                keys[int(i/4)] = w[i:i+4]
    			
        return keys

	      
        
        
     

        
 
    
