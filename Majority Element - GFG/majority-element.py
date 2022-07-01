#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        ele=0
        count = 0
        for i in range(N):
            if count ==0:
                ele = A[i]
            if ele == A[i]:
                count+=1
            else:
                count-=1
        c_ele=0
        for i in range(N):
            if A[i]==ele:
                c_ele+=1
      
        if c_ele<=(N//2):
            return -1
        else:
            return ele
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends