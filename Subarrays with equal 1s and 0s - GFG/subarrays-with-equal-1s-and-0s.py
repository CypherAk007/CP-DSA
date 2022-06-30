#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,a, n):
        freq=0
        d={}
        d[0]=1
        s=0
        for i in range(n):
            if a[i]==0:
               s+=-1
            else:   
                s+=1
            if s in d:
                freq+=d[s]
                d[s]+=1
            else:
                d[s]=1
                
        return freq
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends