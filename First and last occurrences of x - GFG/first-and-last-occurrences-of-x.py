#User function Template for python3


def find(arr,n,x):
    # code here
    res=[]
    fo=first(arr,n,x)
    lo=last(arr,n,x)
    res.append(fo)
    res.append(lo)
    return res

def first(arr,n,x):
    f=-1
    lo=0
    hi=n-1
    while(lo<=hi):
        mid=lo+(hi-lo)//2
        if arr[mid]==x:
            f=mid
            hi=mid-1
        elif x<arr[mid]:
            hi=mid-1
        else:
            lo=mid+1 
    return f
    
def last(arr,n,x):
    l=-1
    lo=0
    hi=n-1
    while(lo<=hi):
        mid=lo+(hi-lo)//2
        if arr[mid]==x:
            l=mid
            lo=mid+1
        elif x<arr[mid]:
            hi=mid-1
        else:
            lo=mid+1 
    return l

#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends