class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        o=[]
        out=[]
        for i in range(len(nums2)-1,-1,-1):
            if len(s)==0:
                out.append(-1)
            elif len(s)>0 and s[-1]>nums2[i]:
                out.append(s[-1])
            elif len(s)>0 and s[-1]<=nums2[i]:
                while len(s)>0 and s[-1]<=nums2[i]:
                    s.pop()
                if len(s)==0:
                    out.append(-1)
                else:
                    out.append(s[-1])
            s.append(nums2[i])
        out.reverse()
        
        for i in range(len(nums1)):
            o.append(out[nums2.index(nums1[i])])
        return o