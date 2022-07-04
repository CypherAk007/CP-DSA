class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        mx=float('-inf')
        d={}
        while(j<len(s)):
            if s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
            
            if len(d)==(j-i+1):
                mx=max(mx,j-i+1)
                # print(mx,d,i,j)
                j+=1
            elif len(d)<(j-i+1):
                while(len(d)<(j-i+1)):
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        d.pop(s[i])
                    i+=1
                j+=1
        if mx==float('-inf'):
            return 0
        return mx
    
# Use of SlidingWindow 