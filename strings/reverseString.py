class Solution:
    '''
    given function reverses the string given in list form
    '''
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp=""
        forwordFlag = 0
        backFlag = len(s)-1
        mid = int(len(s)/2)
        for i in range(mid):
            temp=s[forwordFlag]
            s[forwordFlag]=s[backFlag]
            s[backFlag]=temp
            forwordFlag+=1
            backFlag-=1
        #for i -ends
        
if __name__ == '__main__':
    sol = Solution()
    s=["H","e","l","l","o"]
    sol.reverseString(s)
    print(s)