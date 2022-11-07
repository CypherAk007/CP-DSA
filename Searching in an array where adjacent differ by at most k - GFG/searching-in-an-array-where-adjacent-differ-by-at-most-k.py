#User function Template for python3

def search (arr, n, x, k): 
    #Complete the function
    ans=-1
    i=0
    while(i<n):
        if arr[i]==x:
            ans=i
            break
        y=max(1,abs(arr[i]-x)//k)
        i=i+y 
    return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n, k = map(int , input().split())
    arr = list(map(int, input().strip().split()))
    x = int(input())
    ans = search(arr, n, x, k)
    print(ans)




# } Driver Code Ends