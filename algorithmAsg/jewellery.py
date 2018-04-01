import numpy as np

# |----------------------------------------------------------------------------|
# rodCutting
# |----------------------------------------------------------------------------|
def rodCutting(w, size, inputData):
    '''
    
    '''
    # debug
    print("inputData = {}".format(inputData))
    # debug -ends
#     for j in range(1, size+1):
#         for i in range(1, j+1):
#             print ("i={}, j={}".format(i,j))


    r = np.zeros((size+1))
    r[0]=0
    for j in range(1,size+1):
        q=-99999
        cutIndex = -1
        for i in range(1, j+1):
            # debug
            print(i, inputData[i,2])
           # print("i={}, j={}, max({}, {}+{})".format(i, j,q, inputData[i,2], r[j-i]))
            # debug -ends
            if inputData[i,4]>=0:
                oldQ=q
                if i*inputData[i,3] > j:
                    temp=inputData[i,2]*inputData[i,3]+r[j-i*inputData[i,3]]
                    q=max(q,temp )
                    print("i={},j={},max({},{}+{})".format(i,j,q,inputData[i,2]*inputData[i,3],r[j-i*inputData[i,3]]))
                else:
                    min=inputData[i,3]
                    if min==0:
                        min+=1
                    while(min>0):
                        if(min*i<=j):
                            break
                        min-=1
                    temp=inputData[i,2]*min+r[j-i*min]
                    q=max(q,temp) 
                    print("i={}, j={}, max({},{}+{}".format(i,j,q,inputData[i,2]*min,r[j-i*min]))      
                if oldQ!=q:
                    cutIndex = i
        #for i -ends
        r[j]=q
        if cutIndex!=-1:
            inputData[cutIndex,4]=inputData[cutIndex,4]-1
        # debug
        print("r[{}] = {}".format(j,r[j]))
        # debug -ends
        print("\n")
    #for j -ends

    return r
# |--------------------------------rodCutting---------------------------------|
    


















if __name__ == '__main__':
    w = 20
    size=10
#     inputData = np.array([[0,0,0,0,0,0,0],[1,2,10,8,10,2,2],[2,2,10,8,10,2,4]])
    inputData = np.array([[0,0,0,0,0],\
                          [1,1,1,0,10],\
                          [2,2,5,3,10],\
                          [3,3,8,0,10],\
                          [4,4,9,0,10],\
                          [5,5,10,0,10],\
                          [6,6,17,0,10],\
                          [7,7,17,0,10],\
                          [8,8,20,0,10],\
                          [9,9,24,0,10],\
                          [10,10,30,0,0]])
    ans = rodCutting(w, size, inputData)
    # debug
    print("ans = {}".format(ans))
    # debug -ends
