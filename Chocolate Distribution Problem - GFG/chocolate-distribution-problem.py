#User function Template for python3

class Solution:

    def findMinDiff(self, a,N,M):

        # code here
        a.sort()
        mini=float('inf')
        i=0
        j=M-1 
        while(j<N):
            mini=min(mini,a[j]-a[i])
            i+=1
            j+=1 
        return mini
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends