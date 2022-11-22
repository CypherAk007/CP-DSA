#User function Template for python3

class Solution:
    def maximizeSum(self, a, n, k):
        # Your code goes here
        a.sort()
        for i in range(n):
            if a[i]<0 and k>0:
                a[i]=a[i]*-1
                k-=1 
        if k%2==0 or k==0:
            return sum(a)
        elif k%2==1:
            return sum(a)-2*min(a)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maximizeSum(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends