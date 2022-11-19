class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
	def sortedArrayToBST(self, nums):
	    # code here
	    root= self.helper(nums,0,len(nums)-1)
	    pre=[]
	    self.preorder(root,pre)
	    return pre
	    
    def helper(self,nums,s,e):
        if s>e:
            return None
        mid=(s+e)//2
        root=Node(nums[mid])
        root.left=self.helper(nums,s,mid-1)
        root.right=self.helper(nums,mid+1,e)
        return root
    
    def preorder(self,root,pre):
        if root==None:
            return 
        pre.append(root.data)
        self.preorder(root.left,pre)
        self.preorder(root.right,pre)
#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends