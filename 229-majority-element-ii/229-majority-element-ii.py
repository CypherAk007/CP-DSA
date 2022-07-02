class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        out = []
        nums1=0
        nums2=0
        c1=0
        c2=0
        n=len(nums)
        for i in range(n):
            if nums[i]==nums1:
                c1+=1
            elif nums[i]==nums2:
                c2+=1
            elif c1==0:
                nums1=nums[i]
                c1=1
            elif c2==0:
                nums2=nums[i]
                c2=1
            else:
                c1-=1
                c2-=1
        c1_ele = nums.count(nums1)
        c2_ele = nums.count(nums2)
        print(c1_ele,c2_ele)
        if c1_ele>n//3 and c2_ele>n//3:
            if nums1!=nums2:
                out.append(nums1)
                out.append(nums2)
            else:
                out.append(nums1)
            print(out)
        elif c1_ele>n//3:
            out.append(nums1)
        elif c2_ele>n//3:
            out.append(nums2)
        return out