

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        summ=0
        count=0
        arr=[]
        for i in range(n):
            arr.append([price[i],i+1])
        arr.sort()
        # print(arr)
        for i in range(n):
            # if price[i]>k:
            #     break
            if arr[i][1]*arr[i][0]<=k:
                count+=arr[i][1]
                summ+=arr[i][1]*arr[i][0]
                k-=arr[i][1]*arr[i][0]
            else:
                val=k//arr[i][0]
                count+=val
                summ+=val*arr[i][0]
                k-=val*arr[i][0]
            # print(i,k,price[i],(i+1)*price[i],summ,count)
        return count
                



#{ 
 # Driver Code Starts


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends