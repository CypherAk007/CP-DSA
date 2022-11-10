#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n>m:
            return self.kthElement(arr2,arr1,m,n,k)
        lo=max(0,k-m) # if larger arr is less than k then smaller arr lo cant be 0.
        hi=min(k,n) # if k is < len(smaller arr) then hi cant be len(smaller arr) it should be k.
        while(lo<=hi):
            cut1=lo+(hi-lo)//2
            cut2=k-cut1
            
            # Edges Cases
            if cut1==0:
                l1=float('-inf')
            else:
                l1=arr1[cut1-1]
            
            if cut2==0:
                l2=float('-inf')
            else:
                l2=arr2[cut2-1]
            
            if cut1==n:
                r1=float('inf')
            else:
                r1=arr1[cut1]
            
            if cut2==m:
                r2=float('inf')
            else:
                r2=arr2[cut2]
                
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            elif (l1>r2): #move left
                hi=cut1-1
            else: #move right
                lo=cut1+1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends