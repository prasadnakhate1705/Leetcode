class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        n = len(nums)

        if n==1:
            return nums
        
        l,r= 0,len(nums)-1

        while (l<r):
            if nums[l]%2!=0 and nums[r]%2==0:
                nums[l], nums[r] = nums[r], nums[l]

            elif nums[l]%2==0 and nums[r]%2==0:
                l+=1
                continue 
            elif nums[l]%2!=0 and nums[r]%2!=0:
                r-=1
                continue
            
            l+=1
            r-=1
        
        return nums

        