class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.bs(1,num,num)
    def bs(self,lo,hi,t):
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            x=mid*mid
            if x==t:
                return True
            if t<x:
                hi=mid-1
            else:
                lo=mid+1 
        return False
        