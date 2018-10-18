class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lenA = len(A)
        lenB = len(B)
        newA = A
        times = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a))
        for i in range(2):
            if B in (A * (times + i)):
                return times + i
        return -1
        
            
if __name__ == '__main__':
    A = "abc"
#     B = "cabcabca"
    B = "aabcbabcc"
    sol = Solution()
    count = sol.repeatedStringMatch(A, B)
    # debug
    print("B = {}".format(B))
    print("count = {}".format(count))
    # debug -ends
