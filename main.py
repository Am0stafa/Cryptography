# method generateIC takes a list of cosets as an inputs and returns the IC for these cosets
def generateIC(coset):
    cosetIC = 0
    for c in coset:
        c = c.lower()
        count = [0] * 26
        n = 0
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




# def cosets(list,n):
#     output=[list[i:i + n] for i in range(0, len(list), n)]
#     #check for correct cosets
#     numofw=False
#     for i in range(0,len(output)):
#         if len(output[i]) !=n:
#             for x in range(0,len(output[i])):
#                 output[(numofw%i)].append(output[i][x])
#                 numofw = True
#     if numofw:
#         output.pop()
#
#     return output


def cosets(string,numb):
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


def crack(cipher):
    listOfCos =[]
    sum = 0
    avg =0
    res =-9999999999999
    answer = 0
    for x in range(1,10):
        listOfCos = cosets(cipher,x)
        avg = generateIC(listOfCos)
        if avg > res:
            res = avg
            answer = x

    return answer








s0 = "RSTCSJLSLRSLFELGWLFIISIKRMGL"
s1 = "OICPWZXZEVLGCLNFSYPGALPXWZJTEGALPCSIIWDHOIECCBFWPAHOPCGALPCCBROASNWTYHOIDBIHVPSCSIDEVLSYPGDLZDSLXSTBNWOTTMICPBAPJEVLCLCSUSEQCUHZQFBPPDOUHESSFLLGSUSCPGWINETVVESSZXLEIZUFZMVYNLBXYZESALPXRPWLRFLIHTHOXSPANPZCWMCZCJPPTQMALPXOISFEHOIZYZFXSTBNCZFQHRYZHKSTDWNRZCSALPXPLGLFGLXSPMJLLYULXSTBNWESSFTFDVALPSITEYCOJIQZFDECOOUHHSWSIDZALQLJGLIESSTEDEVLGCLNFSYPGDIDPSNIYTIZFPNOBWPEVLTPZDSIHSCHVPNFHDJPBVYRSHVXSTBRXSPMJEYNVHRRPHOIHZFSHLCSALPZBLWHSCKS"
s2 = "VVVXSQWPSNJMUMJOKKLGFQAVEXAHWRVTMFXVVRKAJTVMFLOPHYWJDSTXKAGFVVTPHKYEPPJOKPSWACJVSIGGVOLXLVMQPVCMGOGMFLAKENVRMIUAKTKVHIXCFJZRAHWFHLIUMHCIRFWGFOETIUNEQVJWEHOSJWVQFYWKYMPGQHWISOPKHYFYV"
#key_length = crack(s0)
print(crack(s2))












