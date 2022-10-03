class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d={}
        for i in wordDict:
            d[i]=1
        dp=[-1]*(len(s)+1)
        x=self.helper(0,s,d,dp)
        return x
    
    def helper(self,i,s,d,dp): # return F/T weather the broken word is possible or not
        # bc
        if i==len(s):
            return True
        
        if dp[i]!=-1:
            return dp[i]
        
        temp=''
        for j in range(i,len(s)):
            temp+=s[j]
            if d.get(temp)!=None: #if this word is there inside the dict
              #if we are further able to break the word then return True
                if (self.helper(j+1,s,d,dp) ==True):
                    dp[i]=True
                    return dp[i]
        dp[i]=False
        return dp[i]
        
        