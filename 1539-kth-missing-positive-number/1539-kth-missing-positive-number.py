class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        end=arr[n-1]+k+1
        j=0
        c=0
        res=0
        for i in range(1,end+1):
            # print(i,j,c,res)
            if c==k:
                res=i-1
                break
            if j<n and arr[j]==i:
                j+=1
            else:
                c+=1
        return res