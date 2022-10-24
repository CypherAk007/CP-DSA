class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)<len(nums2):
            return self.giveinter(nums1,nums2)
        else:
            return self.giveinter(nums2,nums1)

    def giveinter(self,nums1,nums2):
        d={}
        s=set()
        for i in range(len(nums1)):
            if nums1[i] in d:
                d[nums1[i]]+=1
            else:
                d[nums1[i]]=1
        for i in range(len(nums2)):
            if nums2[i] in d:
                s.add(nums2[i])
        return s
        