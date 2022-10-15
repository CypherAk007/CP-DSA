#User function Template for python3
class Solution:
    def minimumNumberOfSwaps(self,s):
        # code here 
        open=0
        close=0
        swaps=0
        unbalanced=0
        for i in range(0,len(s)):
            if s[i]=='[':
                open+=1 
                if unbalanced>0:
                    swaps+=unbalanced
                    unbalanced-=1
            else:
                close+=1 
                unbalanced=close-open 
        return swaps
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        ob = Solution()
        print(ob.minimumNumberOfSwaps(S))
# } Driver Code Ends