class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        rows, cols = len(matrix), len(matrix[0])
        r0 = 0
        c0 = 0
        r1 = rows-1
        c1 = cols-1
        outList = []
        while(r0<=r1 and c0<=c1):
            print(r0<=r1 and c0<=c1)
            for c in range(c0,c1+1):
                outList.append(matrix[r0][c])
            for r in range(r0+1, r1+1):
                outList.append(matrix[r][c1])
            if  c0<c1 and r0<r1:
                for c in range(c1-1, c0, -1):
                    outList.append(matrix[r1][c])
                for r in range(r1, r0, -1):
                    outList.append(matrix[r][c0])
            #if -ends
            r0+=1
            c0+=1
            r1-=1
            c1-=1
        #while -ends
        return outList
    
    
if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    #matrix = [[1,2,3,4],[4,6,7,8],[9,10,11,12]]
    sol = Solution()
    outList = sol.spiralOrder(matrix)
    # debug
    print("outList =\n {}".format(outList))
    # debug -ends
