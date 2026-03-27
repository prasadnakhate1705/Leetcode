class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prefix_sum = 0
        hash_map = {0:-1}


        for i , num in enumerate(nums):
            prefix_sum+=num
            rem = prefix_sum % k

            if rem in hash_map:
                if i-hash_map[rem] >=2 :
                    return True
            else:
                hash_map[rem]=i
        
        return False


        