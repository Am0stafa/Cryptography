class DES:
    def __init__(self,mode,message):
        self.mode = mode
        self.message = message
        
        self.keys = [
        "000110110000001011101111111111000111000001110010",
        "011110011010111011011001110110111100100111100101",
        "010101011111110010001010010000101100111110011001",
        "011100101010110111010110110110110011010100011101",
        "011111001110110000000111111010110101001110101000",
        "011000111010010100111110010100000111101100101111",
        "111011001000010010110111111101100001100010111100",
        "111101111000101000111010110000010011101111111011",
        "111000001101101111101011111011011110011110000001",
        "101100011111001101000111101110100100011001001111",
        "001000010101111111010011110111101101001110000110",
        "011101010111000111110101100101000110011111101001",
        "100101111100010111010001111110101011101001000001",
        "010111110100001110110111111100101110011100111010",
        "101111111001000110001101001111010011111100001010",
        "110010110011110110001011000011100001011111110101"
        ]

        self.p_function = [[16, 7, 20, 21],
              [29, 12, 28, 17],
              [1, 15, 23, 26],
              [5, 18, 31, 10],
              [2, 8, 24, 14],
              [32, 27, 3, 9],
              [19, 13, 30, 6],
              [22, 11, 4, 25]]
    
    
    def Get_S_box(self, number):  # This function takes the number of the S-box and returns the corresponding S-box
    
        # Every S-box is represented as a list of lists
        # Every list in each list of lists represents a row in the corresponding S-box
        s1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
              [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
              [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
              [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
        s2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
              [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
              [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
              [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
        s3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
              [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
              [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
              [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
        s4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
              [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
              [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
              [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
        s5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
              [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
              [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
              [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
        s6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
              [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
              [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
              [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
        s7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
              [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
              [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
              [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
        s8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
              [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
              [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
              [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        switcher = {
            1: s1,
            2: s2,
            3: s3,
            4: s4,
            5: s5,
            6: s6,
            7: s7,
            8: s8
    
        }
        return switcher.get(number)
        
    
    def Substitution(self, value, s_box):  # This function takes a string of 6 bits and the desired s_box as inputs and returns a string of 4 bits after
        row = int(value[0] + value[5], 2)
        column = int(value[1] + value[2] + value[3] + value[4], 2)
        value = bin(s_box[row][column])[2:]
        while len(value) < 4:
            value = '0' + value
        return value
        
    
    def xOR(self, va1,va2):
        res = []
        collector =''
        for x in range(len(va1)):
            a = va1[x]#110011
            b = va2[x]#101011
            res.append(collector)
            collector =''
            for y in range(len(a)):
                if a[y] =='1' and b[y]=='1' or  a[y] == '0' and b[y] == '0':
                    collector +='0'
                elif a[y] == '1' and b[y] == '0' or a[y] == '0' and b[y] == '1' :
                    collector+='1'
        res.pop(0)
        res.append(collector)
        return res
    

    def permute(self,permutation,message):
        permutedMessage = ''
        for x in range(len(permutation)):
            for y in range(len(permutation[x])):
                permutedMessage += message[permutation[x][y]-1] 
        return permutedMessage
    
    
    def divideInto4(self,array):
        result  =[]
        collector = ''
        for x in range(len(array)):
            if x%4 ==0:
                result.append(collector)
                collector=''
            collector+=array[x]
    
        result.pop(0)
        result.append(collector)
        return result
    
    
    def divideInto6(self,array):
        result =[]
        collector = ''
        for x in range(len(array)):
            if x % 6 == 0:
                result.append(collector)
                collector = ''
            collector += array[x]
        result.pop(0)
        zz = ''
        for j in range(6,0,-1):
            zz+=array[-j]
        result.append(zz)
        return result
    
    
    def Ebit(self,arrOf4):
        result = []
        for x in range(len(arrOf4)):
          result.append( arrOf4[(x-1)%len(arrOf4)][-1] + arrOf4[x] + arrOf4[(x+1)%len(arrOf4)][0] )
        return result
        
    def Encrypt(self):
        # Every list in initial_permutation list of lists represents a row in the initial permutation table
        initial_permutation = [ [58, 50, 42, 34, 26, 18, 10, 2],
                                [60, 52, 44, 36, 28, 20, 12, 4],
                                [62, 54, 46, 38, 30, 22, 14, 6],
                                [64, 56, 48, 40, 32, 24, 16, 8],
                                [57, 49, 41, 33, 25, 17, 9, 1],
                                [59, 51, 43, 35, 27, 19, 11, 3],
                                [61, 53, 54, 37, 29, 21, 13, 5],
                                [63, 55, 47, 39, 31, 23, 15, 7] ]
    
        # Every list in e_bit_selection list of lists represents a row in the e_bit_selection_table
        e_bit_Selection = [ [32, 1, 2, 3, 4, 5],
                            [4, 5, 6, 7, 8, 9],
                            [8, 9, 10, 11, 12, 13],
                            [12, 13, 14, 15, 16, 17],
                            [16, 17, 18, 19, 20, 21],
                            [20, 21, 22, 23, 24, 25],
                            [24, 25, 26, 27, 28, 29],
                            [28, 29, 30, 31, 32, 1] ]
    
    
    
        # Every list in final_permutation list of lists represents a row in final_permutation table
        final_permutation = [ [40, 8, 48, 16, 56, 24, 64, 32],
                             [39, 7, 47, 15, 55, 23, 63, 31],
                             [38, 6, 46, 14, 54, 22, 62, 30],
                             [37, 5, 45, 13, 53, 21, 61, 29],
                             [36, 4, 44, 12, 52, 20, 60, 28],
                             [35, 3, 43, 11, 51, 19, 59, 27],
                             [34, 2, 42, 10, 50, 18, 58, 26],
                             [33, 1, 41, 9, 49, 17, 57, 25] ]
    
        # Write your implementation here
    
        #step 1: initial permutation:
        permutedMessage = self.permute(initial_permutation,self.message)
    
        #step 2:divide into L0 and R0
        L0 = permutedMessage[:32]
        R0 = permutedMessage[32:]
        CurrentRound = 0
        l,r = self.leftAndRight(L0,R0,CurrentRound)
    
        # concat l and r
        con = r+l
    
        #final permutation
        result = self.permute(final_permutation,con)
    
        return result
        
    def leftAndRight(self,left,right,counter):

    
        key = self.keys[counter]
    
        #step 3: expand R0 using E-bit
        expandedR0 =''
    
        #divide right into 4
        rightOf4 = self.divideInto4(right)
    
        leftof4 = self.divideInto4(left)
    
        new = self.Ebit(rightOf4)
    
        #divide the key into 6
        keyOf6 = self.divideInto6(key)
    
    
        R0xK = self.xOR(keyOf6,new)
    
    
        Sboxed = []
        #S-box step
        for s in range(len(R0xK)):
            Sboxed.append(self.Substitution(R0xK[s],self.Get_S_box(s+1)))
    
        m = "".join(Sboxed)
    
        permutedR1 = self.permute(self.p_function,m)
    
        permuted4 = self.divideInto4(permutedR1)
    
        #xOR the above with L0 to get final R1
        finalR1 = self.xOR(permuted4,leftof4)
    
        Nleft = "".join(finalR1)
        
        if counter == 15:
            return [right,Nleft]
    
        return self.leftAndRight(right,Nleft,counter+1)

