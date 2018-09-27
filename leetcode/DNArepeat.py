import re
class Solution:
    def check_ValidString(self,string):
        charRe=re.compile(r'[^ACGT]')
        string = charRe.search(string)
        return not bool(string)

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        mapList = []
        opList = []
        mapList.append(s[0:10])
        for i in range(1, len(s)-9):
            str = s[i:i+10]
            print("\n",str)
            print("mapList",mapList)
            print("opList",opList)
            #if len(str)>10:
            if str in mapList and str not in opList:
                opList.append(str)
            else:
                mapList.append(str)
                #if -ends
        #for -ends
        return opList

if __name__ == '__main__':
    s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    solution = Solution()
    opList=solution.findRepeatedDnaSequences(s)
    print(opList)