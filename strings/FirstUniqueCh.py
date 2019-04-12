class Solution:
    def firstUniqChar(self, s: str) -> int:
        myDict = {}
        for ch in s:
            if ch not in myDict:
                myDict[ch]=0
            else:
                myDict[ch]=1
            #if -ends
        #for ch -ends
        for index, ch in enumerate(s):
            if myDict[ch]==0:
                return index
            #if -ends
        #for -ends
        return -1
        
if __name__ == '__main__':
    sol = Solution()
    s="abcda"
    print("index of first unique charector in string:", sol.firstUniqChar(s))
    