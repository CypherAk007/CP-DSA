class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1)==0:
            print(nums2)
            return nums2
        elif len(nums2)==0:
            print(nums1)
            return nums1
        
        i=0
        while(i<m):
            print(i,m)
            if nums1[i]>nums2[0]:
                nums1[i],nums2[0]=nums2[0],nums1[i]
                i+=1
                nums2.sort()#after swapping the array2 is not sorted
            else:
                i+=1
        print(nums1,nums2)
        
        x=m
        y=0
        print('in')
        while(x<len(nums1)and y<n):
            nums1[x]=nums2[y]
            x+=1
            y+=1
            print(nums1,nums2,x,y)
        print('out')
        return
