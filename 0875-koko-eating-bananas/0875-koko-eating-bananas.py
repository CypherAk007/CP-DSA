class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo=1
        hi=max(piles)
        res=hi
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            ans=self.helper(piles,mid)
            if ans<=h:
                res=min(res,mid)
                hi=mid-1
            else:
                lo=mid+1
        return res

    def helper(self,piles,k):
        h=0
        for i in range(len(piles)):
            c=0
            c+=piles[i]//k
            if piles[i]%k!=0:
                c+=1
            h+=c
        return h
               