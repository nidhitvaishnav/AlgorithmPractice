
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #edge case
        if n==0 or n==1:
            return 0

        #create an arr of size n
        arr =[0 for i in range(n)]
        
        #for all numbers in n
        for i in range(2,n):
            #if the number is a prime number
            #find its multiples - non primes
            if arr[i]==0:
                for j in range(i+i,n,i):
                    arr[j]=1
                #for -ends
            #if -ends
        #for -ends
        
        #return total count - non primes - 2(1 and n)
        return n-2-sum(arr)
    
if __name__ == '__main__':
    sol = Solution()
    count = sol.countPrimes(100)
    # debug
    print("count of prime numbers= {}".format(count))
    # debug -ends
