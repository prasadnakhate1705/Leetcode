class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums.copy()
        k= k%len(nums)
        x = len(nums) - k 
        
        nums[:k]=arr[x:]
        nums[k:]= arr[0:x]  

        return nums              


        