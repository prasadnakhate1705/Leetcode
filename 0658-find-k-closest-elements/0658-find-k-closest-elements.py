class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        res = []
        n = len(arr)

        l,r = 0, n-1

        if x > arr[n-1]:
            return arr[n-k:]
        elif x<arr[0]:
            return arr[:k]

        while (l<=r):
            mid = (l+r)//2

            if arr[mid]==x:
                l=r=mid
                break
            
            if arr[mid]<x:
                l = mid+1
            else:
                r = mid-1
        
        i=l-1
        j=l

        while k!=0:
            if 0<=i<=n-1 and 0<=j<=n-1 and abs(arr[i]-x)<=abs(arr[j]-x):
                res.append(arr[i])
                i-=1
                k-=1
            elif 0<=j<=n-1:
                res.append(arr[j])
                j+=1
                k-=1

        return sorted(res)


        

        
        


        






        