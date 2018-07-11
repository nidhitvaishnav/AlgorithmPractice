def findCoOrdinates(x,y,z,n):
    coOrdinateList = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if ((i+j+k)!=n):
                    coOrdinateList.append([i,j,k])
                #if -ends
            #for k -ends
        #for j -ends
    #for i -ends
    return coOrdinateList
#def findCoOrdinates - ends

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print (findCoOrdinates(x,y,z,n))