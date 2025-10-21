class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(len(nums)):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=n+1
        
        for i in range(len(nums)):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1],nums[i]= nums[i],nums[nums[i]-1] 

        for i,num in enumerate(nums):
            if num!=i+1:
                return i+1
        
        return n+1

        

        
        