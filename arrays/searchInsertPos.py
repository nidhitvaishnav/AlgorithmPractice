class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        prevN = None
        for index, i in enumerate(nums):
            if i==target:
                return index
            if i<target:
                prevN = i
            elif ((i>target and prevN==None) or (i>target and prevN<target)):
                return index
        #for -ends
        return index+1
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,5,6]
#     target = 5
#     target = 2
#     target = 7
    target = 0
    ans = sol.searchInsert(nums, target)
    # debug
    print("ans = {}".format(ans))
    # debug -ends
