class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i= 0
        count = 0

        for j in range(len(nums)):
            if nums[j]!=0:
                count+=1
                nums[i] = nums[j]
                i+=1
        
        for k in range(count, len(nums)):
            nums[k]=0
        
    
        