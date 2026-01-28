class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # count = 0
        # for num in nums:
        #     count+=1
    
        # while(count!=0):
        #     for i in range(len(nums)-1):
        #         if nums[i]==0 and nums[i+1]!=0:
        #             nums[i], nums[i+1] = nums[i+1], nums[i]
            
        #     count-=1

        w =0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[w]=nums[i]
                w+=1
        
        while w!=len(nums):
            nums[w]=0
            w+=1

            
        return nums
    
        