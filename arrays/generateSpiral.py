class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n<=0:
            return []
        if n==1:
            return [[1]]

        matrix = [[0 for i in range(n)] for j in range(n)] 
        r0 = 0
        c0 = 0
        r1 = n-1
        c1 = n-1
        i=1
        while(r0<=r1 and c0<=c1):
            for c in range(c0,c1+1):
                matrix[r0][c]=i
                i+=1
            for r in range(r0+1, r1+1):
                matrix[r][c1]=i
                i+=1
            if  c0<c1 and r0<r1:
                for c in range(c1-1, c0, -1):
                    matrix[r1][c]=i
                    i+=1
                for r in range(r1, r0, -1):
                    matrix[r][c0]=i
                    i+=1
            #if -ends
            r0+=1
            c0+=1
            r1-=1
            c1-=1
        #while -ends
        return matrix
    
    
if __name__ == '__main__':
    n=5
    sol = Solution()
    matrix = sol.generateMatrix(n)
    print(matrix)