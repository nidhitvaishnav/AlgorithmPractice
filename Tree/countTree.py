class MyTree:
# |----------------------------------------------------------------------------|
# findPossibleTreeGivenNode
# |----------------------------------------------------------------------------|
    def findPossibleTreeGivenNode(self, n):
        '''
        
        '''
        if n<0:
            return 0
        if n==0 or n==1:
            return 1
        count=0
        for i in range(1,n+1):
            count+=self.findPossibleTreeGivenNode(i-1)*self.findPossibleTreeGivenNode(n-i)                                                                              
        #for i -ends
        
        return count
        
# |--------------------------------findPossibleTreeGivenNode---------------------------------|
        
        
        
if __name__ == '__main__':
    n=3
    myTree = MyTree()
    ans = myTree.findPossibleTreeGivenNode(n)
    print("Possible trees given {} nodes: {}".format(n,ans))