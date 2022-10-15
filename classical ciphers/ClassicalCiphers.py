class ClassicalCiphers:
    def __init__(self):
        pass
        
    def caesarEncrypt(self,text,s):
        result = ""
     
        for i in range(len(text)):
            char = text[i]
     
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
     
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
     
        return result
        

    def caesarDecrypt(self,text,s):
        result = ""
     
        for i in range(len(text)):
            char = text[i]
     
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) - s-65) % 26 + 65)
     
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) - s - 97) % 26 + 97)
     
        return result
        
    # encrypts text with the Vigenere cipher
    def vigenereEncrypt(self,text, key):
        result = ""
     
        # traverse text
        for i in range(len(text)):
            char = text[i]
     
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + ord(key[i % len(key)]) - 2 * 65) % 26 + 65)
     
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + ord(key[i % len(key)]) - 2 * 97) % 26 + 97)
     
        return result
    # decrypts text with the Vigenere cipher
    def vigenereDecrypt(self,text, key):
        result = ""
     
        # traverse text
        for i in range(len(text)):
            char = text[i]
     
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) - ord(key[i % len(key)]) + 26) % 26 + 65)
     
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) - ord(key[i % len(key)]) + 26) % 26 + 97)
     
        return result
        
    # encrypts text with the Playfair cipher
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
    # encrypts text with monoalphabetic substitution
    def monoalphabeticEncrypt(self,text, key):
        result = ""
     
        # traverse text
        for i in range(len(text)):
            # get current character
            char = text[i]
            # check if space
            if (char == ' '):
                result += ' '
            else:
                # add corresponding character from key
                result += key[ord(char) - 65]
     
        return result
    # decrypts text with monoalphabetic substitution
    def monoalphabeticDecrypt(self,text, key):
        result = ""
     
        # traverse text
        for i in range(len(text)):
            # get current character
            char = text[i]
            # check if space
            if (char == ' '):
                result += ' '
            else:
                # add corresponding character from key
                result += chr(key.index(char) + 65)
     
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