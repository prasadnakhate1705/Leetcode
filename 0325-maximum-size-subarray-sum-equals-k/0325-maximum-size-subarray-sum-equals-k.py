class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        
        prefix_map = {0:-1}
        curr_sum =0
        max_len = 0

        for i in range(len(nums)):
            curr_sum+=nums[i]

            if (curr_sum -k) in prefix_map:
                max_len = max(max_len, (i-prefix_map[curr_sum - k]) )
            
            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i
        
        return max_len
            
    
        


