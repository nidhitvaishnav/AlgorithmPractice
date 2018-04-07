P = [0, 1, 5, 8, 10, 13, 17, 17, 20, 24, 26]

def optimalMaxRevenue(n):
    R = [0 for i in range(0,n+1)]
    S = [0 for i in range(0,n+1)]
    for k in range(1,n+1):
        for i in range(1, k+1):
            if(R[k] < P[i] + R[k-i]):
                R[k] = P[i] + R[k-i]
                S[k] = i
                
    return R,S

def findSol(S, n):
    l = n
    sol = []
    while(l > 0):
        sol.append(S[l])
        l = l - S[l]
    return sol



if __name__ == '__main__':
	# main()

	R, S = optimalMaxRevenue(10)

	print("P:", P)
	print("R:",R)
	print(S)
	print(findSol(S, 10))