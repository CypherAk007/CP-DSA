class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # itrative math(factorial) sol.
        numbers=[]
        fact=1
        # First we compute the factorial of n-1
        for i in range(1,n):
            fact=fact*i
            numbers.append(i) #array which stores all numbers
        numbers.append(n) #last no. is appended here
        ans=""
        k=k-1 # 0-based indexing 17th perm==> 16th perm
        while(True): # Runs till the numbers array is not empty
            ans=ans+str(numbers[k//fact]) # we get the first no idx(2). 3 _ _ _   
            numbers.pop(k//fact)# we remove the 3 to get new array ie.[1,2,4]
            if len(numbers)==0:
                break
                
            k=k%fact #next k val ie the remaining amount
            # 1st time blocks were of size 6 next it was of size 2-one fact less
            fact=fact//len(numbers) 
            
        return ans
        