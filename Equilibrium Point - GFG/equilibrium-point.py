# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        if len(A)==1:
            return 1
            
        p=[0 for i in range(N) ]
        s=[0 for i in range(N) ]
        # print(p,s)
        for i in range(1,N):
            p[i]=A[i-1]+p[i-1]
        # print(p)
        for i in range(N-2,-1,-1):
            s[i]=A[i+1]+s[i+1]
        # print(s)
        for i in range(N):
            if s[i]==p[i] and s[i]!=0:
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