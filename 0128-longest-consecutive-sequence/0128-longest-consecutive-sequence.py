class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## Convert it into set for o(1)- lookup
        nums_set = set(nums)
        
        longest = 0

        for n in nums_set:
            if n-1 not in nums_set:
                #For a new sequence
                length=1
                new_n = n+1
                while new_n in nums_set:
                    length+=1
                    new_n+=1
                longest = max(longest, length)
        
        return longest



        
            





        