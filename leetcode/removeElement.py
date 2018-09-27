class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        numLen = len(nums)
        if numLen==0:
            return 0
        i=-1
        for j in range(0, numLen):
            if nums[j]!=val:
                i+=1
                nums[i]=nums[j]
            #if -ends
        #for -ends
        return i+1
    
    
if __name__ == '__main__':
    solution = Solution()
    nums=[2]
    ans = solution.removeElement(nums, 3)
    for i in range(0, ans):
        print(nums[i])