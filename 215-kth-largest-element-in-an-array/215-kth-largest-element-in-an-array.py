class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Implement using Quick Select
        
#         self.quickSelect(nums,0,len(nums)-1,k-1)
#     #     return sorted(nums)[-k]
#     # tell the 5th smallest element
#     def quickSelect(self,arr,lo,hi,k):
#       pivot=arr[hi]
#       pi=self.partition(arr,pivot,lo,hi)
#       if k>pi:#kth index>pivot index then search in right part
#         return self.quickSelect(arr,lo,pi-1,k)
#       elif k<pi:
#         return self.quickSelect(arr,pi+1,hi,k)
#       else:
#         return pivot

#     def partition(self,arr,pivot,lo,hi):
#       # i-end - unknown
#       # 0- j-1- small
#       # j- i-1  -big elements
#       i=lo
#       j=lo
#       while(i<=hi):
#         if (arr[i]<=pivot):
#           arr[i],arr[j]=arr[j],arr[i]
#           i+=1
#           j+=1
#         else:
#           i+=1
#       return j-1#returns pivot position


    
    
    # usingheaps
    
        import heapq
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,nums[i])
            while(len(heap)>k):
                heapq.heappop(heap)
        return heap[0]