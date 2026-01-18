class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        m = len(nums)

        hash_map = {}
        
        for i in range(m):

            if nums[i] not in hash_map:
                hash_map[nums[i]]=0
            
            if hash_map[nums[i]]==1:
                return nums[i]
            
            hash_map[nums[i]]+=1

        