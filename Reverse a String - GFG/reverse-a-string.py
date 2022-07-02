#User function Template for python3

# def reverseWord(s): # convert to lst reverse convert back
#     #your code here
#     lst=list(s)
#     # print(lst)
#     i=0
#     j=len(lst)-1
#     while(i<j):
#         lst[i],lst[j]=lst[j],lst[i]
#         i+=1
#         j-=1
        
#     return "".join(lst)
        
def reverseWord(s): # Using recursion
    if len(s)==0:
        return s
    else:
        return reverseWord(s[1:])+ s[0]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends