class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mySet = []
        maxChar = 0
        for i in s:
            if i in mySet:
                index = mySet.index(i)
                mySet = mySet[index+1:]
            #if -ends
            mySet.append(i)
            if maxChar<len(mySet):
                maxChar = len(mySet)
            #if maxChar -ends
        #for i -ends
        return maxChar
    
if __name__ == '__main__':
    s = "abcabcbb"
    s = "bbbbb"
    s = "pwwkew"
    
    sol = Solution()
    ans = sol.lengthOfLongestSubstring(s)
    # debug
    print("ans = {}".format(ans))
    # debug -ends
