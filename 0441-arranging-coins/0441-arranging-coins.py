class Solution:
    def arrangeCoins(self, n: int) -> int:
        t=n
        c=0
        for i in range(1,n+1):
            if i<=t:
                t-=i
                c+=1 
            if i>t:
                break
        return c