class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # n=len(num)
        # i=n-1
        # lst=[]
        # while(i>=0 or k>0):
        #     if i>=0:
        #         lst.append((num[i]+k)%10)
        #         k=(num[i]+k)//10
        #         # print(i,lst,k)
        #         i-=1
        #     else:
        #         lst.append(k%10)
        #         k=k//10
        #         # print(i,lst,k)
        # lst.reverse()
        # return lst
        # # return list(originalNo+k)
          c=k
          ext=[]
          for i in range(len(num)-1,-1,-1):
            if c==0:
              break
            val=c+num[i]
            num[i]=val%10
            val=val//10
            c=val
            # print(num,val,c,k)
          if c!=0:
            while c!=0:
              ext.append(c%10)
              c//=10
            ext.reverse()
            for i in range(len(num)):
              ext.append(num[i])
            return ext
          return num