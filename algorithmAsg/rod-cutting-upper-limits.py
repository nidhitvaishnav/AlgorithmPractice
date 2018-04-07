from __future__ import print_function

# p = [ 0,  1, 5,  8, 10, 13, 17, 17, 20, 24, 26]
# p = [ 0,  1,  5,  8,  9, 10, 17, 17, 20, 24, 30]
# x = [ 0, 10,  10, 10, 10, 10,  10, 10, 10, 10,  0]
# w = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = [0, 10, 10]
x = [0, 10, 10]
w = [0,  2,  2]
n = [0, 8, 8]
f = [0, 2, 2]
c = [0, 2, 4]

def printTable(R):
    print("\t", end="")
    for i in range(len(R[0])):
        print(i, end="\t")
    print()
    for i in range(len(w )):
        print(i,"\t", end=" ")
        for j in range(len(R[i])):
            print(R[i][j], end="\t")
        print()

def optimalMaxRevenue(G):
    R = [[0 for i in range(0, G+1)] for j in range(0, len(w))]

    for i in range(1, len(w)):
        print("n[i] =", n[i])
        print("\n\n\nItem", i,",weight of item being made:", w[i])
        # q = R[i-1][k]
        for k in range(1, G+1):
            # q = R[i-1][k]
            q=-9999999999
            print("\n\nlocal total gold:", k)
            for q_i in range(0, x[i] + 1):
                if(k-q_i*w[i] >= 0):

                    total_fine = 0
                    if(f[i]*(n[i] - q_i)>=0):
                        total_fine = min(f[i]*(n[i] - q_i), c[i])
                    print("Fine:", total_fine)
                    print("\nq_i", q_i)
                    print("val1:", q)
                    print("val2:", q_i*p[i] + R[i-1][k-q_i*w[i]] - total_fine)
                      
                    q = max(q, q_i*p[i] + R[i-1][k-q_i*w[i]] - total_fine)
            print("opt:", q)
            R[i][k] = q
    printTable(R)

if __name__ == '__main__':
	R = optimalMaxRevenue(20)