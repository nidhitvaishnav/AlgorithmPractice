class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        tmpStr=  ""
        for i in range(len(s)):
            #odd case
            tmpStr = self.checkPalindrome(s,i,i)
            if len(tmpStr)>=len(ans):
                ans = tmpStr
            #if -ends
            #even case
            tmpStr = self.checkPalindrome(s,i,i+1)
            if len(tmpStr)>=len(ans):
                ans=tmpStr
            #if -ends
        #for -ends
        return ans
    
    def checkPalindrome(self,s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        #while -ends
        return s[l+1:r]
    
if __name__ == '__main__':
    str = "amadamb"
    sol = Solution()
    ans = sol.longestPalindrome(str)
    print(ans)