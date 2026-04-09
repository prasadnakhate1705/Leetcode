class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        curr_sum = 0
        l = 0
        min_len = len(nums)+1

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                min_len = min(min_len, r-l+1)
                curr_sum-=nums[l]
                l+=1
        
        return 0 if min_len==len(nums)+1 else min_len

            

        