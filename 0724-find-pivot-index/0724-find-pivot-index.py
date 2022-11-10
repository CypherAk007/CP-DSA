class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        # prefix sum
        pre=nums[:]
        for i in range(1,n):
            pre[i]=pre[i-1]+pre[i]
        pre.pop()
        pre.insert(0,0)
        # print(pre)
        
        # postfix sum
        post=nums[:]
        # print(post)
        for i in range(n-2,-1,-1):
            post[i]=post[i+1]+post[i]
        post.append(0)
        post.pop(0)
        # print(post)
        
        for i in range(n):
            if self.check(i,nums,pre,post)==True:
                return i
        return -1
    def check(self,i,nums,pre,post):
        if pre[i]==post[i]:
            return True
        return False