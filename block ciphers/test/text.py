import numpy as np

key_PBox = [14,    17,   11,    24,     1,    5,
                  3,    28,   15,     6,    21,   10,
                 23,    19,   12,     4,    26,    8,
                 16,     7,   27,    20,    13,    2,
                 41,    52,   31,    37,    47,   55,
                 30,    40,   51,    45,    33,   48,
                 44,    49,   39,    56,    34,  53,
                 46,    42,   50,    36,    29,   32]



def keypermute(key16):
    keypermuted = np.empty([16,48])
    l = 0
    for k in key16:
        j = 0
        for i in key_PBox:
            keypermuted[l][j] = k[i - 1]
            j += 1
        l += 1
    return keypermuted
    
def keyshift(toshift,n):
    if (n == 1) or (n == 2) or (n == 9) or (n == 16):
        toshift= np.roll(toshift,-1)
        return toshift
    else:
        toshift = np.roll(toshift, -2)
        return toshift
        
def keyschedule(key):
    left = key[0:28]
    right = key[28:56]
    shifted = np.zeros(56)
    key16 = np.zeros([16,56])
    for i in range(1,17):
        shifted[0:28] = keyshift(left,i)
        shifted[28:56] = keyshift(right,i)
        left = shifted[0:28]
        right = shifted[28:56]
    #add shifted to key16 and return key16
        key16[i - 1] = shifted
    #key16 is the final shifted 16 key pair now to permute
    key16 = keypermute(key16)
    key16 = [list(map(int, x)) for x in key16]
    key16 = np.array(key16)
    #convert numpy array into array
    keyMet = [list(map(int, key)) for key in key16]
    for i in range(0,16):
        keyMet[i] = "".join(map(str, keyMet[i]))
    
    
    return keyMet

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(str(int(bin(i)[2:])))
  return m

def formateKey(key):
    binaryKey = toBinary(key)
    strKey = "".join(binaryKey)
    if len(strKey) > 56:
        strKey = strKey[:56]
    keys = []
    for i in strKey:
        keys.append(i)
    return keys    


def main():
    
    # key = ['1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0',   '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0']
        #^ length of the key must be 56

    key = (formateKey("abdomostaaa"))
    
    # print(len('000110110000001011101111111111000111000001110010'))
    # print(len('100110011110001011011000101010011001111111011111'))
    
    key16 = keyschedule(key)
    
    # print(key16)


  

main()
