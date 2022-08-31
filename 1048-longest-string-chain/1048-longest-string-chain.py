class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words=sorted(words,key=len)
        n=len(sorted_words)
        dp=[1]*(n)
        maxi=1
        for i in range(0,n):
            for prev in range(0,i):
                if self.checkPossible(sorted_words[i],sorted_words[prev]) and 1+dp[prev]>dp[i]: 
                    #whenever the dp array is getting updated
                    dp[i]=1+dp[prev]
                    
            if dp[i]>maxi:
                maxi=dp[i]
        
        return maxi
    
    def checkPossible(self,s1,s2): #length of s1>s2
        if len(s1)!=len(s2)+1:
            return False
        first=0
        second=0
        while(first<len(s1)):
            if (second<len(s2) and s1[first]==s2[second]):
                first+=1
                second+=1
            else:
                first+=1 #bcde and bde if ptr is at idx 1 the only first is inc.
        if first==len(s1) and second==len(s2):
            return True
        return False