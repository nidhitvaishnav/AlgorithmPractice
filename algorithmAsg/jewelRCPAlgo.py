import sys
import numpy as np
# from jewel import Jewel

# |============================================================================|
class Jewel:
# |============================================================================|
# |----------------------------------------------------------------------------|
# __init__
# |----------------------------------------------------------------------------|
    def __init__(self, w, p, n, x, f, c):
        '''
        storing values to object of type jewel
        '''
        self.w = w
        self.p = p
        self.n = n
        self.x = x
        self.f = f
        self.c = c
# |--------------------------------__init__------------------------------------|

# |============================================================================|
class JewelRCPAlgo:
# |============================================================================|
# |----------------------------------------------------------------------------|
# optimalMaxRevenue
# |----------------------------------------------------------------------------|
    def optimalMaxRevenue(self, G, jewelList):
        '''
        based on G and jewelList, return optimal solution and number of possible
        optimal solution
        '''
        #initialization
        n = len(jewelList)
        MaxRevenue = np.zeros((n,G+1))
        SolutionCount = np.zeros((n,G+1))
        
        for j in range(0, G+1):
            SolutionCount[0][j] = 1
        
        #FINDING OPTIMUM SOLUTION
        #going through all items
        for i in range(1, n):
            #going through all the possible values of G
            for g in range(0, G+1):
                #initializing q to -inf
                q=-99999
                #going through all the possible count of items which is less 
                #than max count
                for q_i in range(0, jewelList[i].x + 1):
                    #if (g-qiwi>=0)
                    if(g-q_i*jewelList[i].w >= 0):
                        fine = 0
                        #if (ni-qi>0)
                        if( jewelList[i].n-q_i > 0):
                            fine = min((jewelList[i].n - q_i)*jewelList[i].f,\
                                                             jewelList[i].c)
                        #if ni-qi>0 -ends
                        current_gain = jewelList[i].p*q_i - fine \
                                                        + MaxRevenue[i-1][g \
                                                        - q_i*jewelList[i].w]
                        q = max(q, current_gain)
                    #if g-qi*wi>=0 -ends
                #for qi -ends

                #assigning the max revenue to MaxRevenue array
                MaxRevenue[i][g]=q
                
                #calculating count as we have got final MaxRevenue
                for q_i in range(0, jewelList[i].x + 1):
                    #if (g-qiwi>=0)
                    if(g - q_i*jewelList[i].w >= 0):
                        fine = 0
                        #if (ni-qi>0)
                        if(jewelList[i].n - q_i > 0):
                            fine = min((jewelList[i].n - q_i)*jewelList[i].f,\
                                                         jewelList[i].c) 
                        #checking for optimum solution
                        if(MaxRevenue[i][g] == MaxRevenue[i-1][g - q_i*jewelList[i].w]\
                                                 + jewelList[i].p*q_i - fine):
                            SolutionCount[i][g] = SolutionCount[i][g] +\
                                                     SolutionCount[i-1][g - q_i\
                                                            *jewelList[i].w]
                        #if optimum condition -ends
                    #if g-qi*wi>=0 -ends
                #for qi -ends
            #for g -ends
        #for i -ends
        return MaxRevenue, SolutionCount
        
# |--------------------------------optimalMaxRevenue---------------------------------|
# |----------------------------------------------------------------------------|
# enumerateSolution
# |----------------------------------------------------------------------------|
    def enumerateSolution(self,s, jewelList, MaxRevenue, g, i):
        '''
        printing entire solution using recursion
        '''
        #base case
        if i == 0:
            for element in s[1:]:
                print(element, end=" ")
            print()
        #induction step
        else:
            for q_i in range(0, jewelList[i].x + 1):
#                 # debug
#                 print("q+i = {}".format(q_i))
#                 # debug -ends

                #calculating optimal solution
                if(g-q_i*jewelList[i].w >= 0):
                    #fine calculation
                    fine = 0
                    if jewelList[i].n - q_i > 0:
                        fine = min((jewelList[i].n-q_i)*jewelList[i].f, \
                                                            jewelList[i].c)
                    #check for the optimal solution
                    if(MaxRevenue[i][g] == MaxRevenue[i-1][g \
                                                - q_i*jewelList[i].w]\
                                                + jewelList[i].p*q_i - fine):
                        s[i] = q_i
                        self.enumerateSolution(s, jewelList, MaxRevenue,\
                                                    g - q_i*jewelList[i].w, i-1)
# |--------------------------------enumerateSolution---------------------------|
    
    
# |----------------------------------------------------------------------------|
# readDataFromFile
# |----------------------------------------------------------------------------|
    def readDataFromFile(self, filePath):
        
        '''
        read Data from file
        '''
        #Initialization
        count = 0
        n=0
        inputList = []
        #read file into input list
        with open(filePath) as file:
            for line in file:
                #on the first line we have G and n
                if count==0:
                    G, n = [int(i) for i in line.split(" ")]
                #read next lines till count is less than n+2 
                #(less than or equal to n+1 as 1st is the G, n line) 
                elif (count<n+2):
                    intLine = [int(i) for i in line.split(" ")]
                    inputList.append(intLine)
                count+=1
        return G, n, inputList
# |--------------------------------readDataFromFile----------------------------|
# |----------------------------------------------------------------------------|
# dataCleaning
# |----------------------------------------------------------------------------|
    def dataCleaning(self, inputList):
        '''
        input: inputList which contains all the data in 2D list
        output: jewelList which has objects of item with w,p,n,x,f,c values
        '''
        
        cols = len(inputList)
        jewelList = []
        jewel = Jewel(0,0,0,0,0,0)
        jewelList.append(jewel)
        
        #storing data in objects
        for i in range(cols):
            w = inputList[i][1]
            p = inputList[i][2]
            n = inputList[i][3]
            x = inputList[i][4]
            f = inputList[i][5]
            c = inputList[i][6]
            jewel = Jewel(w,p,n,x,f,c)
            jewelList.append(jewel)
        #for i -ends
        return jewelList
        
# |--------------------------------dataCleaning--------------------------------|
    





if __name__ == '__main__':
    jewelRCPAlgo =  JewelRCPAlgo()
    printSolutionFlag = False
    #if no arguments are given or, 2nd argument is "-"
    if ((len(sys.argv)==1) or (len(sys.argv)==2 and sys.argv[1]=="-")):
        G, n= [int(i) for i in input().split(" ")]
        lineData = []
        for i in range(n):
            intLine = [int(i) for i in input().split(" ")]
            lineData.append(intLine)
    #if 2 or 3 arguemnts are given, than 2nd arg is file name, read data from file
    elif (len(sys.argv)==2 or len(sys.argv)==3):
        print('system argm = {}'.format(sys.argv))
        filePath = sys.argv[1]
        G, n, lineData = jewelRCPAlgo.readDataFromFile(filePath)
        #if 3rd arguement is greater than 0, than print the solution
        if(len(sys.argv)==3 and int(sys.argv[2])>0):
            printSolutionFlag=True
    else:
        print("Parameters are not given properly")
        exit()
    #if sys.argv -ends

    #storing data in object list
    jewelList = jewelRCPAlgo.dataCleaning(lineData)
    n=len(jewelList)
#     # debug
#     for obj in jewelList:
#         print(obj.w, obj.p, obj.n, obj.x, obj.f, obj.c)
#     # debug -ends

    #finding optimal max revenue and total number of optimal solution
    MaxRevenue, solutionCount = jewelRCPAlgo.optimalMaxRevenue(G, jewelList)
    # debug
    print("Optimum solution = {}".format(MaxRevenue[-1][-1]))
    print("Total number of optimum solution = {}".format(solutionCount[-1][-1]))
    # debug -ends
    
    #print the enumeration of solution if 3rd arguement is greater than 0
    if printSolutionFlag:
        s = [-1 for j in range(0, n)]
        jewelRCPAlgo.enumerateSolution(s, jewelList, MaxRevenue, G, n-1)
    #if printSolutionFlag -ends