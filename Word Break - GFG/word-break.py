#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this function
    d={}
    for i in dictionary:
        d[i]=1 
    dp=[-1]*len(line)
    return helper(0,line,d,dp)
    
def helper(pos,s,d,dp):
    # bc
    if pos == len(s):
        return True
    
    if dp[pos]!=-1:
        return dp[pos]
    
    temp=''
    for i in range(pos,len(s)):
        temp+=s[i]
        if d.get(temp)!=None and helper(i+1,s,d,dp)==True:
            dp[pos]=True
            return dp[pos]
    dp[pos]=False
    return dp[pos]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends