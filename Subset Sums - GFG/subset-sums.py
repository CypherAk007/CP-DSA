#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		return self.sub(0,arr)
	def sub(self,p,up):
        if len(up)==0:
            lst=[]
            lst.append(p)
            return lst 
      
        digit=up[0]
        l=self.sub(p+digit,up[1:])
        r=self.sub(p,up[1:])
        l+=r
        return l 
	    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends