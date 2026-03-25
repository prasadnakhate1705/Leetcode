class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        fans = nums[0]

        for num in nums:
            ans+=num
            fans = max(fans, ans)
            
            if ans<0:
                ans = 0
        
        return fans
        