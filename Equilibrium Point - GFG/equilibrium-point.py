# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        p=[]
        p[:]=A[:]
        s=[]
        s[:]=A[:]
        # print(A)
        # prefixSum
        for i in range(1,len(p)):
            p[i]=p[i]+p[i-1]
        # print(s)
        # suffixSum
        for i in range(len(s)-2,-1,-1):
            s[i]=s[i]+s[i+1]
        # print(s)
        for i in range(len(s)):
            if s[i]==p[i]:
                return i+1
        return -1
        
        


#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends