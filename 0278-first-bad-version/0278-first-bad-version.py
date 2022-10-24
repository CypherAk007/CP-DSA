# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.bs(n)
    def bs(self,n):
        lo=1
        hi=n
        res=0
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            x=isBadVersion(mid)
            if x==True:
                res=mid
                hi=mid-1
            elif x==False:
                lo=mid+1
        return res
        