#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        res=[]
        vis=[0]*n
        for i in range(n):
            if vis[i]==0:
                vis[i]=1
                temp=[]
                temp.append(words[i])
                d=self.makedict(words[i])
                c=len(d)
                # print(d,c)
                for j in range(i+1,n):
                    if self.checkanagram(words[j],c,d.copy()):
                        temp.append(words[j])
                        vis[j]=1
                    # print(words[i],words[j],temp)
                res.append(temp)
                
        return res
    
    def makedict(self,word):
        d={}
        for i in range(len(word)):
            if word[i] in d:
                d[word[i]]+=1 
            else:
                d[word[i]]=1 
        return d
        
    def checkanagram(self,w,c,d):
        for i in range(len(w)):
            if w[i] in d:
                d[w[i]]-=1
                if d[w[i]]==0:
                    c-=1 
        if c==0:
            return True
        else:
            return False
            
            
            
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