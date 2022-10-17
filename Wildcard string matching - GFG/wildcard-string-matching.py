#User function Template for python3

class Solution:
    def match(self, wild, pattern):
        # code here
        # recursive sol
        dp=[[-1]*(len(pattern)+1) for i in range(len(wild)+1)]
        return self.helper(len(wild),len(pattern),wild,pattern,dp)
    def helper(self,i,j,s1,s2,dp):
        # bc
        if i==0 and j==0:
            return True
        if i==0 and j>0:
            return False
        if i>0 and j==0:
            for k in range(1,i):
                if s1[k]=='*':
                    return True
                else:
                    return False
        if dp[i][j]!=-1:
            return dp[i][j]
            
        if s1[i-1]==s2[j-1] or s1[i-1]=='?':
            dp[i][j]= self.helper(i-1,j-1,s1,s2,dp)
            return dp[i][j]
        
        if s1[i-1]=='*':
            dp[i][j]= self.helper(i-1,j,s1,s2,dp) or self.helper(i,j-1,s1,s2,dp)
            return dp[i][j]
        return False
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        wild = input()
        pattern = input()
        
        ob = Solution()
        if(ob.match(wild, pattern)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends