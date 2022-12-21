#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this function
    d={}
    for i in dictionary:
        d[i]=1 
    return helper(0,line,d)
    
def helper(pos,s,d):
    # bc
    if pos == len(s):
        return True
    
    temp=''
    for i in range(pos,len(s)):
        temp+=s[i]
        if d.get(temp)!=None and helper(i+1,s,d)==True:
            return True
    return False


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