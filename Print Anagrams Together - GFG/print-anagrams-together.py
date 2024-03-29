#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        d={}
        for i in range(len(words)):
            x=self.sortandreturn(words[i])
            if x in d:
                d[x].append(words[i])
            else:
                d[x]=[words[i]]
        res=[]
        for i in sorted(d):
            res.append(d[i])
        return res
                
    def sortandreturn(self,w):
        temp=list(w)
        temp.sort()
        return ''.join(temp)
            
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends