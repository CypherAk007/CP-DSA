class Solution:
    def mySqrt(self, x: int) -> int:
        res=0
        for i in range(x+1):
            if i*i<=x:
                res=i   
            if i*i>x:
                break
        return res