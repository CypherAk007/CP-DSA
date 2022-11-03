#User function Template for python3

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # code here
        res=[] #[val/kg,val,wt]
        for i in range(n):
            vec=[]
            vec.append(Items[i].value/Items[i].weight)
            vec.append(Items[i].value)
            vec.append(Items[i].weight)
            res.append(vec)
            
        # sort acc to the per kg value for max value
        res.sort(key=lambda x: x[0],reverse=True)
        # print(res)
        
        totalValue=0
        for i in range(n):
            if W==0:
                return totalValue
            # if current item wt is > bag wt then only fraction wt is considered
            if res[i][2]>W:
                totalValue+= W*res[i][0] #remaining wt * per kg val
                W=0
            else:
                totalValue+=res[i][1]#value
                W=W-res[i][2]
        return totalValue


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends