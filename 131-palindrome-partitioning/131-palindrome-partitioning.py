from copy import copy
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.helper(s,[],[])
    def helper(self,s,temp,ans):
        if not s:
            ans.append(temp)
            return 
        for i in range(1,len(s)+1):
            sub = s[:i]
            if sub==sub[::-1]:
                self.helper(s[i:],temp+[sub],ans)
        return ans