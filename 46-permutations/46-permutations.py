# from copy import copy
class Solution:
    def permute(self, s):
        p=[]
        up=s
        ans=[]
        self.all(p,up,ans)
        return ans
    def all(self, p,up,ans)->list[list]:
        if len(up) == 0:
            ans.append(p)
            return 
        ch = up[0]
        for i in range(len(p) + 1):
            f = p[0:i]
            s = p[i:]
            self.all(f+[ch]+s, up[1:], ans)
        return ans