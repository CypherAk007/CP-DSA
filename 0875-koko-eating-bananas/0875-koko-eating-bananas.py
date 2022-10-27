class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo=1
        hi=max(piles)
        res=0
        while(lo<hi):
            mid=lo+(hi-lo)//2
            ans=self.helper(piles,mid)
            # print(ans,mid)
            if ans>h:
                lo=mid+1
            else :
                hi=mid
            
            
        return hi

    def helper(self,piles,k):
        h=0
        for i in range(len(piles)):
            c=0
            c+=piles[i]//k
            if piles[i]%k!=0:
                c+=1
            h+=c
        return h
               