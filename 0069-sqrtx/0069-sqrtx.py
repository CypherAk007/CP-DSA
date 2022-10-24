class Solution:
    def mySqrt(self, x: int) -> int:
        return self.bs(x)
    def bs(self,x):
        lo=0 
        hi=x
        res=-1
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            val=mid*mid
            if val==x:
                return mid
            elif x<val:
                hi=mid-1
            elif x>val:
                res=mid
                lo=mid+1 
        return res