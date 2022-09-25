class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=[]
        q.append([list(beginWord),1]) #word,level
        d={}
        wl=[]
        for i in wordList:
            wl.append(tuple(i))

        
        for i in wl:
            d[i]=0

        while(len(q)!=0):

            n=q.pop(0)
            word=n[0]
            steps=n[1]
            
            if word==list(endWord):
                return steps
            
            # now we have to change every char in the word
            # word=hat
            
            for i in range(0,len(word)):
                # 0th char -h

                original=word[i] #char that we are looking to change
                for ch in range(ord('a'),ord('z')+1):
                    # 0th got replaced
                    # aat , bat ,cat,...zat
                    word[i]=chr(ch)

                    # if the word exists in the dict and not visited
                    if tuple(word) in d :
                        d.pop(tuple(word))
                        x=word[:]
                        q.append([x,steps+1])

                        
                word[i]=original

        return 0 