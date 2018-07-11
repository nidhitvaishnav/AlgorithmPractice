class LeafNode:

# |----------------------------------------------------------------------------|
# __init__
# |----------------------------------------------------------------------------|
    def __init__(self, keyList, valueList, next_page):
        '''
        
        '''
        self.keyList = keyList
        self.valueList = valueList
        self.nextPage = next_page
        
# |--------------------------------__init__---------------------------------|
# |----------------------------------------------------------------------------|
# isLeafValid
# |----------------------------------------------------------------------------|
    def isLeafValid(self):
        '''
        
        '''
        nKeys = len(self.keyList)
        nValues = len(self.valueList)
        validFlag = False
        if nKeys==nValues:
            validFlag=True
        #if -ends
        return validFlag
# |--------------------------------isLeafValid---------------------------------|
    

class InteriorNode:

# |----------------------------------------------------------------------------|
# __init__
# |----------------------------------------------------------------------------|
    def __init__(self, keyList, pointerList):
        '''
        
        '''
        self.keyList = keyList
        self.pointerList = pointerList
# |--------------------------------__init__---------------------------------|
# |----------------------------------------------------------------------------|
# isInteriorNodeValid
# |----------------------------------------------------------------------------|
    def isInteriorNodeValid(self):
        '''
        
        '''
        nKeys = len(self.keyList)
        nPointer = len(self.pointerList)
        validFlag = False
        if ((nKeys+1)==nPointer):
            validFlag=True
        #if -ends
        return validFlag
        
# |--------------------------------isInteriorNodeValid---------------------------------|
# |----------------------------------------------------------------------------|
# getBeforePagePointer
# |----------------------------------------------------------------------------|
    def getBeforePagePointer(self, key):
        '''
        
        '''
        index = self.keyList.index(key)
        return self.pointerList[index]
# |--------------------------------getBeforePagePointer---------------------------------|
# |----------------------------------------------------------------------------|
# getAfterPagePointer
# |----------------------------------------------------------------------------|
    def getAfterPagePointer(self, key):
        '''
        
        '''
        index = self.keyList.index(key)
        return self.pointerList[index+1]
# |--------------------------------getAfterPagePointer---------------------------------|


class BPlusTree:
# |----------------------------------------------------------------------------|
# __init__
# |----------------------------------------------------------------------------|
    def __init__(self, maxPointer, maxLeafItem):
        '''
        
        '''
        self.nPointer = maxPointer
        self.nLeafVal = maxLeafItem
# |--------------------------------__init__---------------------------------|
        

# |----------------------------------------------------------------------------|
# search
# |----------------------------------------------------------------------------|
    def search(self, nodeObj, key):
        '''
        
        '''
        if (nodeObj.__class__.__name__ == "leafNode"):
            '''return root'''
        else:
            if key<nodeObj.keyList[0]:
                return self.search(nodeObj.getBeforePagePointer(0), key)
            elif key>nodeObj.keyList[-1]:
                return self.search(nodeObj.getAfterPagePointer(-1), key)
            else:
                keyLen = len(nodeObj.keyList)
                for i in range(1, keyLen-1):
                    if nodeObj.keyList[i]<=key and nodeObj.keyList[i+1]>key:
                        return self.search(nodeObj.getAfterPagePointer(i), key)        
                        break;
                    #if -ends
                #for i -ends
            #else -ends
# |--------------------------------search---------------------------------|


if __name__ == '__main__':
    l = LeafNode([1,2],[2,3],1)
    # debug
    print("l class = {}".format(l.__class__.__name__))
    # debug -ends
