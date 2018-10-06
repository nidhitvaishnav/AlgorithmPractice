class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
                print(nums)
                if nums[i-1] > 0:
                    nums[i] += nums[i-1]
        return max(nums)











if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    ans = sol.maxSubArray(nums)
    # debug
    print("ans = {}".format(ans))
    # debug -ends
