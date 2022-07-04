class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums))
    
    def mergeSort(self,a,s,e):
        invpair=0
        if e-s==1:
            return 0
        mid = (s+e)//2
        invpair=self.mergeSort(a,s,mid)
        invpair+=self.mergeSort(a,mid,e)
        invpair+=self.merge(a,s,e,mid)
        return invpair

    def merge(self,a,s,e,mid):

        revpair=0
        jth=mid
        for val in range(s,mid):
            while jth<e and a[val]>(2*a[jth]):
                jth+=1
            revpair+=(jth-(mid))

        i=s
        j=mid
        k=0
        mix = [0 for i in range(e-s)]
        # print(mix)
        while(i<mid and j<e):

            if (a[i]<a[j]):
                mix[k]= a[i]
                i+=1 
            else:
                mix[k]=a[j]
                j+=1 
            k+=1 
        while(i<mid):
            mix[k]=a[i]
            i+=1 
            k+=1
        while(j<e):
            mix[k]=a[j]
            j+=1 
            k+=1
        for x in range(len(mix)):
            a[s+x]=mix[x]
        return revpair