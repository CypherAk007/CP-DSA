class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        dist=[]
        heaters.sort()
        
        for i in range(len(houses)):
            ans=self.bscf(heaters,houses[i])
            
            # appends closest dist fmhouse to left and right heaters
            dist.append(min(abs(houses[i]-ans[0]),abs(houses[i]-ans[1]))) 

        return max(dist)

        
    def bscf(self,heaters,t): #finds both ceil and floor together
        ans=[float('inf'),float('inf')]
        n=len(heaters)
        lo=0
        hi=n-1
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if heaters[mid]==t:
                ans[0]=heaters[mid]
                break
            if t<heaters[mid]:
                ans[1]=heaters[mid]
                hi=mid-1
            else:
                ans[0]=heaters[mid]
                lo=mid+1
        return ans