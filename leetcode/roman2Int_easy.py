class Solution:
    
    #-----------------push--------------------------------#
    def push(self, char,stack, stackLen):
        stack=stack+char
        stackLen+=1
        print("push:", stack)
        print("push:", stackLen)
        return stack, stackLen
    #-----------push -ends--------------------------------#
    #------------------pop--------------------------------#
    def pop(self, stack, stackLen):
        if stackLen>-1:
            char = stack[stackLen]
            stack=stack[:stackLen]
            stackLen-=1
            print("pop:", stack)
            print("pop:", stackLen)
            return char, stack, stackLen
        #if -ends
        return "", stack, stackLen
    #------------pop -ends--------------------------------#
    #------------------isValid----------------------------# 
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #stack
        stack=""
        stackLen=-1
        #take  opening, put it in the stack, pop the stack when you get closing paranthesis
        for char in s:
            if (char=='(' or char=='{' or char=='['):
                stack, stackLen=self.push(char, stack, stackLen)
            else:
                if stackLen==-1:
                    return False
                stackChar, stack, stackLen=self.pop(stack, stackLen)
                if ((stackChar=='(' and char!=')') or (stackChar=='[' and char!=']') or (stackChar=='{' and char!='}')):
                    return False
                #if char compare -ends
            #if -ends
        #for -ends
        if stackLen!=-1:
            return False
        return True
    
if __name__ == '__main__':
    s="]"
    solution=Solution()
    ans = solution.isValid(s)
    print(ans)