# unbounded knapsack

# C = 7
# wt = [0, 1, 2, 3]
# val = [0, 1, 3, 2]
# n = 3

C = 20
wt = [0, 2, 2]
val = [0, 10, 10]
n = 2


dp = [0 for i in range(C+1)]

# print(len(dp))
# print(dp)

for c in range(1, C+1):
	print ("Capacity:", c)
	for j in range(1, n+1):
		print ("Item:", j)
		if wt[j] <= c :
			# print("Item:", j, "Weight:", wt[j])
			print ("dp[c] =", "dp[", c, "]:", dp[c])
			print ("dp[c-wt[j]] + val[j] =", "dp[",c,"-", wt[j],"] + ", val[j], ":",  dp[c-wt[j]]+ val[j]) 
			dp[c] = max(dp[c], dp[c-wt[j]]+ val[j]);
			print ("max:", dp[c])
		print
	print
	print

print(dp)