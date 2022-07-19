import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        d={}
        out=[]
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for key,v in d.items():
            heapq.heappush(heap,[v,key])
            while(len(heap)>k):
                heapq.heappop(heap)
        while(len(heap))>0:
            out.append(heap[0][1])
            heapq.heappop(heap)
        return out