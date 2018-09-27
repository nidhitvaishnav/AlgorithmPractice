def solution(A):
#initialization
    lenA = len(A)
    myDict = {}
    
    #for loop that goes over entire Array A
    for i in range(0, lenA-1):
        ii1Str = str(A[i])+"_"+str(A[i+1])
        i1iStr = str(A[i+1])+"_"+str(A[i])
        #check for consicutiveness
        if (ii1Str in myDict):
            myDict[ii1Str]+=1
        if(i1iStr in myDict):
            myDict[ii1Str]=myDict[ii1Str]+1
        if(ii1Str not in myDict) or (i1iStr not in myDict):
            myDict[ii1Str]=int(2)
        #if -ends
    #for -ends
    
    
    return 0


if __name__ == '__main__':
    A = [1,2,1,3,4,3,5,1,2]
    ans = solution(A)