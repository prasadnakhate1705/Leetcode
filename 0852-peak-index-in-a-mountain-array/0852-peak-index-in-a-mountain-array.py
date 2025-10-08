class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        s,l = 0, len(arr)-1

        while s<l:
            mid = (s+l)//2

            if arr[mid]<arr[mid+1]:
                s = mid+1
            else:
                l = mid
            
        return l
            
        




            


            



        