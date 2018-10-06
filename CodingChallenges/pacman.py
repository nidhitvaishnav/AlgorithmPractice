# Complete the pacmanScore function below.
def pacmanScore(mat):
    rows = len(mat)
    cols = len(mat[0])
    print(rows, cols)
    if rows==1 and cols==1:
        return mat[0]
    #if -ends
    #creating solution matrix
    sol = [[0 for x in range(cols)] for y in range(rows)]
    print(sol)
    #initializing 1st column
    for i in range(1, rows):
        print("\ni:",i,"sol[i][0]:", sol[i][0],"sol[i-1][0]:", sol[i-1][0], "mat[i][0]:", mat[i][0])
        sol[i][0]=sol[i-1][0]+ mat[i][0] 
        print(sol[i][0])
        print(sol)
    #for - -ends
    print("After col initialization:\n",sol)
    #initializing 1st row
    for j in range(1, cols):
        sol[0][j]=sol[0][j-1]+mat[0][j]
    #for j -ends
    print(sol)
    for i in range(1, rows):
        for j in range(1, cols):
            if (sol[i-1][j]>sol[i][j-1]):
                sol[i][j]=sol[i-1][j]+mat[i][j]
            else:
                sol[i][j]=sol[i][j-1]+mat[i][j]
            #if -ends
        #for j -ends
    #for i -ends
        # res = -1
        # for j in range(cols):
        #     if j<cols-1 and i<rows-1:
        #         mat[i][j]+=mat[i][j+1] + mat[i+1][j]
        #     elif j <cols - 1:
        #          mat[i][j]+= mat[i][j+1]
        #     elif i<rows-1:
        #          mat[i][j]+= mat[i+1][j]
        # res = max(res, mat[i][j])
    return sol[rows-1][cols-1]


if __name__ == '__main__':
    mat = [[0,3,2,8],[1,4,9,3],[6,2,2,0]]
    ans = pacmanScore(mat)
    print(ans)