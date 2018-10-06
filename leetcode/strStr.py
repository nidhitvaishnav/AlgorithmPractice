class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenH = len(haystack)
        lenN = len(needle)
        if lenN==0:
            return 0
        minHLen = lenH-lenN
        if minHLen==0 and haystack==needle:
            return 0
        for i in range(minHLen+1):
            # debug
            print("haystack[i:i+lenN] = {}".format(haystack[i:i+lenN]))
            # debug -ends

            if haystack[i:i+lenN]==needle:
                return i
            #if -ends
        #for -ends
        return -1
    
if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
#     haystack = "aaaaa"
#     needle = "bba" 
#     haystack = "a"
#     needle="a"
#     haystack = "mississippi"
#     needle = "pi"
    sol=Solution()
    ans = sol.strStr(haystack, needle)
    # debug
    print("ans = {}".format(ans))
    # debug -ends
