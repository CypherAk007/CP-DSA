#User function Template for python3

class Solution:
    def minimumDays(self, S, N, M):
        # code here
        sunday=S//7
        buyingdays=S-sunday
        totFood=S*M
        ans=0
        if totFood%N==0:
            ans=totFood//N
        else:
            ans=totFood//N +1
        if ans<=buyingdays:
            return ans
        else:
            return -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, M = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.minimumDays(S, N, M))
# } Driver Code Ends