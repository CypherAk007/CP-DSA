class Solution:
    def minWindow(self, a: str, t: str) -> str:
        if len(t)>len(a):
            return ''
        d={}
        for i in range(len(t)):
            if t[i] not in d:
                d[t[i]]=1 
            else:
                d[t[i]]+=1
        # print(d)
        count=len(d)
        i=0
        j=0
        
        mini=float('inf')
        minstr=''
        while(j<len(a)):
            if a[j] in d:
                d[a[j]]-=1 
                if d[a[j]]==0:
                    count-=1
            
            if count>0:
                j+=1 
                
            if count==0:
                while(count==0):
                    if mini>(j-i+1):
                        mini=j-i+1
                        minstr=a[i:j+1]
                    # mini=min(mini,j-i+1)
                
                    if a[i] in d:
                        d[a[i]]+=1 
                        if d[a[i]]==1:
                            count+=1 
                    i+=1 
                j+=1
                    
                    # if count==0:
                    #     mini=min(mini,j-i+1)
                    
        if mini==float('inf'):
            return ''
        return minstr
        