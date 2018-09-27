import re
# Complete the analyze_dna function below.
def check_ValidString(string):
    charRe=re.compile(r'[^ACGT]')
    string = charRe.search(string)
    return not bool(string)

def analyze_dna(strands, codon_mapping):
    refinedList = []
    for str in strands:
        length = len(str)
        #print(length)
        #print(charSet)
        if ((length>10 and length<100) and check_ValidString(string=str)):
            refinedList.append(str)
        #if -ends
    #for -ends
    #print("refinedList:",refinedList)
    opStr=""
    
    if len(refinedList)>2:
        flagList=[False]*len(refinedList)
#         tempRefinedList = refinedList[:]

        opStr = string_merge(refinedList, opStr)
    #if -ends
    return opStr


def string_merge(refinedList, opStr):
#     if (len(refinedList) <= 1):
#         return refinedList
    flag = [False]*len(refinedList)
    for index1, i in enumerate(refinedList):
        for index2, j in enumerate(refinedList):
            if((flag[index1]==False and flag[index2]==False) and i[-3:]==j[0:3]):
                opStr+=i+j[3:]
                flag[index1]=True
                flag[index2]=True
            
                
            #ifends
        #for -ends
    #for -ends
#     temp=refinedList[:]
#     for i in temp:
#         if (opStr[-3:]==i[0:3]):
#             opStr+=i[3:]
# #     return string_merge(refinedList, opStr)
    return(opStr)



if __name__ == '__main__':
    strands = ['AGTGGGGGGGGG', 'AAACCCAATTT', 'TTTACACAGCT', 'GCTGGGCCCAGT']
    codon_mapping = ['Afd', 'Cerg', 'Gferg', 'Tsdga']
    analyze_dna(strands, codon_mapping)