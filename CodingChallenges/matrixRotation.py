# Complete the rotateMatrix function below.
def rotateMatrix(mat):
    rows=len(mat)
    for i in range(0, int(rows/2)):
        for j in range(i, rows-i-1):
            temp = mat[i][j]
            mat[i][j]=mat[rows-1-j][i]
            mat[rows-1-j][i]=mat[rows-1-i][rows-1-j]
            mat[rows-1-i][rows-1-j]=mat[j][rows-1-i]
            mat[j][rows-1-i] = temp
        #for j -ends
    #for -i ends
    return mat

if __name__ == '__main__':
    mat = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]
    ans = rotateMatrix(mat)
    n=len(mat)

    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        #for -ends
        print()