class Solution:
    def arrangeCoins(self, n: int) -> int:
        return self.bs(0,n,n)
    def bs(self,lo,hi,n):
        res=-1
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            x=(mid*(mid+1))//2
            print(lo,hi,mid,x,res)
            if x==n:
                return mid
            elif x>n:
                hi=mid-1
            else:
                res=mid
                lo=mid+1
        return res