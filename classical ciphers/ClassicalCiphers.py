import string 
import matplotlib.pyplot as plt

class ClassicalCiphers:
    def __init__(self):
        pass
        
    #! ------------------ caesar ------------------
    
    def caesarEncrypt(self,text,key):
        result = ""
     
        for i in range(len(text)):
            char = text[i]
     
            if (char.isupper()):
                result += chr((ord(char) + key-65) % 26 + 65)
     
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
     
        return result
        
    def caesarDecrypt(self,text,key):
        result = ""
     
        for i in range(len(text)):
            char = text[i]
     
            if (char.isupper()):
                result += chr((ord(char) - key-65) % 26 + 65)    
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
     
        return result
        
    def crackCaesar(self,text):
        for i in range(26):
            print(i, self.caesarDecrypt(text, i))
    
        
    #! ------------------ monoalphabetic substitution ------------------
    
    def monoalphabeticEncrypt(self,text, key):
        result = ""
     
        for i in range(len(text)):
            char = text[i]

            if (char == ' '):
                result += ' '
            else:
                result += key[ord(char) - 65]
     
        return result

    def monoalphabeticDecrypt(self,text, key):
        result = ""
     
        for i in range(len(text)):
            char = text[i]

            if (char == ' '):
                result += ' '
            else:
                result += chr(key.index(char) + 65)
     
        return result
    
    #! ------------------ Vigenere cipher ------------------
    
    def vigenereEncrypt(self,text, key):
        result = ""
     
        for i in range(len(text)):
            char = text[i]
     
            if (char.isupper()):
                result += chr((ord(char) + ord(key[i % len(key)]) - 2 * 65) % 26 + 65)
            else:
                result += chr((ord(char) + ord(key[i % len(key)]) - 2 * 97) % 26 + 97)
     
        return result

    def vigenereDecrypt(self,text, key):
        result = ""
     
        for i in range(len(text)):
            char = text[i]
     
            if (char.isupper()):
                result += chr((ord(char) - ord(key[i % len(key)]) + 26) % 26 + 65)
            else:
                result += chr((ord(char) - ord(key[i % len(key)]) + 26) % 26 + 97)
     
        return result 
        
    @classmethod
    def generateIC(self,coset):
        cosetIC = 0
        for c in coset:
            c = c.lower()
            count = [0] * 26
            n = 1
            for i in range(0, len(c)):
                val = ord(c[i]) - ord('a')
                if (val >= 0 and val <= 25):
                    count[val] = count[val] + 1
                    n += 1
            total = 0.0
            for i in range(0, len(count)):
                total += count[i] * (count[i] - 1)
            total = total / (n * (n - 1))
            cosetIC += total
        cosetIC = cosetIC / len(coset)
        return cosetIC
    
    @classmethod
    def cosets(self,string,numb):
        chars = []
        chars[:] = string
        temp = []
        res = []
        counter=0
        start =0
        for i in range(0, 3):
            for x in range(i, len(chars),numb):
                temp.append(chars[x])
                counter+=1
    
            res.append(''.join(temp[start:]))
            start = counter
    
    
        return res

    def getTheLengthOfVigenereKey(self,cipher):
        listOfCos =[]
        sum = 0
        avg =0
        res =float('-inf')
        answer = 0
        for x in range(1,10):
            listOfCos = self.cosets(cipher,x)
            avg = self.generateIC(listOfCos)
            if avg > res:
                res = avg
                answer = x
    
        return answer
    
    def crackVigenere(self,cipher):
        key = ""
        length = self.getTheLengthOfVigenereKey(cipher)
        cosets = self.cosets(cipher,length)
        for coset in cosets:
            key += self.findMostCommonLetter(coset)
        return key
    
    #* #* #* #* #* #*
    #& #& #& #& #& #& 
    #^ #^ #^ #^ #^ #^
    #! ------------------ Playfair cipher ------------------
    
    def playfairEncrypt(self,text, key):
        result = ""
     
        # generate 5x5 key square
        key = self.removeDuplicates(key)
        key = self.formatKey(key)
        keySquare = self.generateKeySquare(key)
     
        # traverse text
        for i in range(0, len(text), 2):
            # check if pair is valid
            if (i < len(text) - 1 and text[i] == text[i + 1]):
                text = text[:i + 1] + 'X' + text[i + 1:]
     
            # check if length is odd
            if (len(text) % 2 != 0):
                text += 'X'
     
            # get current digraph
            digraph = text[i:i + 2]
     
            # get current digraph locations
            loc = self.getDigraphLocation(digraph, keySquare)
     
            # same row
            if (loc[0][0] == loc[1][0]):
                # replace with letters to right respectively
                result += keySquare[loc[0][0]][(loc[0][1] + 1) % 5]
                result += keySquare[loc[1][0]][(loc[1][1] + 1) % 5]
     
            # same column
            elif (loc[0][1] == loc[1][1]):
                # replace with letters below respectively
                result += keySquare[(loc[0][0] + 1) % 5][loc[0][1]]
                result += keySquare[(loc[1][0] + 1) % 5][loc[1][1]]
     
            # rectangle
            else:
                # replace with letters on same row respectively but at the other pair of corners of the rectangle
                result += keySquare[loc[0][0]][loc[1][1]]
                result += keySquare[loc[1][0]][loc[0][1]]
     
        return result
    # decrypts text with the Playfair cipher
    def playfairDecrypt(self,text, key):
        result = ""
     
        # generate 5x5 key square
        key = self.removeDuplicates(key)
        key = self.formatKey(key)
        keySquare = self.generateKeySquare(key)
     
        # traverse text
        for i in range(0, len(text), 2):
            # get current digraph
            digraph = text[i:i + 2]
     
            # get current digraph locations
            loc = self.getDigraphLocation(digraph, keySquare)
     
            # same row
            if (loc[0][0] == loc[1][0]):
                # replace with letters to left respectively
                result += keySquare[loc[0][0]][(loc[0][1] - 1) % 5]
                result += keySquare[loc[1][0]][(loc[1][1] - 1) % 5]
     
            # same column
            elif (loc[0][1] == loc[1][1]):
                # replace with letters above respectively
                result += keySquare[(loc[0][0] - 1) % 5][loc[0][1]]
                result += keySquare[(loc[1][0] - 1) % 5][loc[1][1]]
     
            # rectangle
            else:
                # replace with letters on same row respectively but at the other pair of corners of the rectangle
                result += keySquare[loc[0][0]][loc[1][1]]
                result += keySquare[loc[1][0]][loc[0][1]]
     
        return result
    
    # encrypts text with the Hill cipher
    def hillEncrypt(self,text, key):
        result = ""
     
        # generate key matrix for multiplication
        keyMatrix = self.generateKeyMatrix(key, len(text))
     
        # traverse text
        for i in range(0, len(text), len(key)):
            # create vector for multiplication
            vect = self.generateVect(text, i, len(key))
     
            # multiply key matrix and vector
            for j in range(len(key)):
                c = 0
                for k in range(len(key)):
                    c += (keyMatrix[j][k] * vect[k])
                c = c % 26
                result += chr(c + 65)
     
        return result
    # decrypts text with the Hill cipher
    def hillDecrypt(self,text, key):
        result = ""
     
        # generate key matrix for multiplication
        keyMatrix = self.generateKeyMatrix(key, len(text))
        # find multiplicative inverse
        inverseKeyMatrix = self.findInverse(keyMatrix)
     
        # traverse text
        for i in range(0, len(text), len(key)):
            # create vector for multiplication
            vect = self.generateVect(text, i, len(key))
     
            # multiply key matrix and vector
            for j in range(len(key)):
                c = 0
                for k in range(len(key)):
                    c += (inverseKeyMatrix[j][k] * vect[k])
                c = c % 26
                result += chr(c + 65)
     
        return result
    # encrypts text with the Autokey cipher
    def autokeyEncrypt(self,text, key):
        result = ""
     
        # append key to text
        text = key + text
     
        # traverse text
        for i in range(len(key), len(text)):
            # get current character
            x = text[i]
            # get previous character
            y = text[i - len(key)]
            # add them together
            result += chr(((ord(x) + ord(y)) % 26) + 65)
     
        return result
        
    # decrypts text with the Autokey cipher
    def autokeyDecrypt(self,text, key):
        result = ""
     
        # traverse text
        for i in range(len(text)):
            # get current character
            x = text[i]
            # get previous character
            if (i < len(key)):
                y = ord(key[i]) - 65
            else:
                y = ord(result[i - len(key)]) - 65
            # subtract them
            result += chr(((ord(x) - y + 26) % 26) + 65)
     
        return result
        
        
    # encrypts text with railfence cipher
    def railfenceEncrypt(self,text, key):
        result = ""
     
        # create matrix to cipher plain text key = rows, length(text) = columns
        # filling the rail matrix to distinguish filled spaces from blank ones
        rail = [['\n' for i in range(len(text))] for j in range(key)]
     
        # to find the direction
        dir_down = False
        row, col = 0, 0
     
        for i in range(len(text)):
            # check the direction of flow
            # reverse the direction if we've just filled the top or bottom rail
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
     
            # fill the corresponding alphabet
            rail[row][col] = text[i]
            col += 1
     
            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
     
        # now we can construct the cipher using the rail matrix
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result += rail[i][j]
     
        return result
        
    # decrypts text with railfence cipher
    def railfenceDecrypt(self,text, key):
        result = ""
     
        # create matrix to cipher plain text key = rows, length(text) = columns
        # filling the rail matrix to distinguish filled spaces from blank ones
        rail = [['\n' for i in range(len(text))] for j in range(key)]
     
        # to find the direction
        dir_down = None
        row, col = 0, 0
     
        # mark the places with '*'
        for i in range(len(text)):
            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
     
            # place the marker
            rail[row][col] = '*'
            col += 1
     
            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
     
        # now we can construct the fill the rail matrix
        index = 0
        for i in range(key):
            for j in range(len(text)):
                if ((rail[i][j] == '*') and (index < len(text))):
                    rail[i][j] = text[index]
                    index += 1
     
        # now read the matrix in zig-zag manner to construct the resultant text
        row, col = 0, 0
        for i in range(len(text)):
            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
     
            # place the marker
            if (rail[row][col] != '*'):
                result += rail[row][col]
                col += 1
     
            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
     
        return result
        
    # encrypts text with row transposition cipher
    def rowTranspositionEncrypt(self,text, key):
        result = ""
     
        # create matrix to cipher plain text key = rows, length(text) = columns
        # filling the rail matrix to distinguish filled spaces from blank ones
        rail = [['\n' for i in range(len(text))] for j in range(key)]
     
        # to find the direction
        dir_down = False
        row, col = 0, 0
     
        for i in range(len(text)):
            # check the direction of flow
            # reverse the direction if we've just filled the top or bottom rail
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
     
            # fill the corresponding alphabet
            rail[row][col] = text[i]
            col += 1
     
            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
     
        # now we can construct the cipher using the rail matrix
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result += rail[i][j]
     
        return result
        
    # decrypts text with row transposition cipher
    def rowTranspositionDecrypt(self,text, key):
        result = ""
     
        # create matrix to cipher plain text key = rows, length(text) = columns
        # filling the rail matrix to distinguish filled spaces from blank ones
        rail = [['\n' for i in range(len(text))] for j in range(key)]
     
        # to find the direction
        dir_down = None
        row, col = 0, 0
     
        # mark the places with '*'
        for i in range(len(text)):
            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
     
            # place the marker
            rail[row][col] = '*'
            col += 1
     
            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
     
        # now we can construct the fill the rail matrix
        index = 0
        for i in range(key):
            for j in range(len(text)):
                if ((rail[i][j] == '*') and (index < len(text))):
                    rail[i][j] = text[index]
                    index += 1
     
        # now read the matrix in zig-zag manner to construct the resultant text
        row, col = 0, 0
        for i in range(len(text)):
            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
     
            # place the marker
            if (rail[row][col] != '*'):
                result += rail[row][col]
                col += 1
     
            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
     
        return result
    # encrypts text with column transposition cipher
    def columnTranspositionEncrypt(self,text, key):
        result = ""
     
        # create matrix to cipher plain text key = rows, length(text) = columns
        # filling the rail matrix to distinguish filled spaces from blank ones
        rail = [['\n' for i in range(len(text))] for j in range(key)]
     
        # to find the direction
        dir_down = False
        row, col = 0, 0
     
        for i in range(len(text)):
            # check the direction of flow
            # reverse the direction if we've just filled the top or bottom rail
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
     
            # fill the corresponding alphabet
            rail[row][col] = text[i]
            col += 1
     
            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
     
        # now we can construct the cipher using the rail matrix
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result += rail[i][j]
     
        return result
    # decrypts text with column transposition cipher
    def columnTranspositionDecrypt(self,text, key):
        result = ""
     
        # create matrix to cipher plain text key = rows, length(text) = columns
        # filling the rail matrix to distinguish filled spaces from blank ones
        rail = [['\n' for i in range(len(text))] for j in range(key)]
     
        # to find the direction
        dir_down = None
        row, col = 0, 0
     
        # mark the places with '*'
        for i in range(len(text)):
            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
     
            # place the marker
            rail[row][col] = '*'
            col += 1
     
            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
     
        # now we can construct the fill the rail matrix
        index = 0
        for i in range(key):
            for j in range(len(text)):
                if ((rail[i][j] == '*') and (index < len(text))):
                    rail[i][j] = text[index]
                    index += 1
     
        # now read the matrix in zig-zag manner to construct the resultant text
        row, col = 0, 0
        for i in range(len(text)):
            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
     
            # place the marker
            if (rail[row][col] != '*'):
                result += rail[row][col]
                col += 1
     
            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
     
        return result
     

    # frequency analysis
    def frequencyAnalysis(self,text):
        # count the frequency of each letter
        count = [0] * 26
        for i in range(0, len(text)):
            val = ord(text[i]) - ord('a')
            if (val >= 0 and val <= 25):
                count[val] = count[val] + 1
        return count

    # we can use the frequency analysis to find the most common letter in the text
    
    def findMostCommonLetter(self,text):
        count = self.frequencyAnalysis(text)
        max = 0
        for i in range(0, len(count)):
            if (count[i] > count[max]):
                max = i
        return chr(max + ord('a'))
    
    # we can use the frequency analysis to find the least common letter in the text
    
    def findLeastCommonLetter(self,text):
        count = self.frequencyAnalysis(text)
        min = 0
        for i in range(0, len(count)):
            if (count[i] < count[min]):
                min = i
        return chr(min + ord('a'))
    #draws a histogram of the frequency of each letter in the text
    def drawHistogram(self,text):
        count = self.frequencyAnalysis(text)
        plt.bar(range(len(count)), count, align='center')
        plt.xticks(range(len(count)), list(string.ascii_lowercase))
        plt.show()


    # Affine cipher
    def affineEncrypt(self,text, key):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) + key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        return result
        
    def affineDecrypt(self,text, key):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) - key - 65) % 26 + 65)
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
        return result
    
    #ADFGX Cipher
    def adfgxEncrypt(self,plainText, key):
        #generate the adfgx table
        table = self.generateADFGXTable(key)
        #generate the cipher text
        cipherText = self.generateADFGXCipherText(plainText, table)
        return cipherText

    def generateADFGXTable(self,key):
        #generate the adfgx table
        table = [['a','d','f','g','x'],['a','d','f','g','x'],['a','d','f','g','x'],['a','d','f','g','x'],['a','d','f','g','x']]
        #generate the key
        key = self.generateKey(key)
        #generate the table
        table = self.generateTable(table, key)
        return table
        
    def generateADFGXCipherText(self,plainText, table):
        #generate the cipher text
        cipherText = ""
        for i in range(0, len(plainText)):
            for j in range(0, 5):
                for k in range(0, 5):
                    if (plainText[i] == table[j][k]):
                        cipherText += self.getLetter(j) + self.getLetter(k)
        return cipherText
        
    def decryptADFGX(self,cipherText, key):
        #generate the adfgx table
        table = self.generateADFGXTable(key)
        #generate the plain text
        plainText = self.generateADFGXPlainText(cipherText, table)
        return plainText
        
    def generateADFGXPlainText(self,cipherText, table):
        #generate the plain text
        plainText = ""
        for i in range(0, len(cipherText), 2):
            plainText += table[self.getNumber(cipherText[i])][self.getNumber(cipherText[i + 1])]
        return plainText
        
    def getNumber(self,letter):
        if (letter == 'a'):
            return 0
        elif (letter == 'd'):
            return 1
        elif (letter == 'f'):
            return 2
        elif (letter == 'g'):
            return 3
        elif (letter == 'x'):
            return 4
        else:
            return -1