class AESKeyExpansion:
    def Expand_key(self, master_key,n_rounds,s_box,r_con):
        #! Initialize round keys with raw key material.
        key_columns = self.bytes2matrix(master_key)
        iteration_size = len(master_key) // 4

        i = 1
        while len(key_columns) < (n_rounds + 1) * 4:
            #! previous word
            word = list(key_columns[-1])

            #! Perform schedule_core once every row
            if len(key_columns) % iteration_size == 0:
                #! Circular shift.
                word.append(word.pop(0))
                #! Map to S-BOX.
                word = [s_box[b] for b in word]
                #! XOR with first byte of R-CON, since the others bytes of R-CON are 0.
                word[0] ^= r_con[i]
                i += 1
            elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
                # Run word through S-box in the fourth iteration when using a
                # 256-bit key.
                word = [s_box[b] for b in word]

            # XOR with equivalent word from previous iteration.
            word = self.xor_bytes(word, key_columns[-iteration_size])
            key_columns.append(word)  # type: ignore

        # Group key words in 4x4 byte matrices.
        return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]
        
    def bytes2matrix(self,text):
        #! loops through tha array of bytes and convert each charter to its asci value
        return [list(text[i:i+4]) for i in range(0, len(text), 4)]

    def xor_bytes(self,a, b):
        return bytes(i^j for i, j in zip(a, b))