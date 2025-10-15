class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)
        ans = 0
        if n==0:
            return 0
        if n==1:
            return nums[0]

        temp1 = max(nums[0],nums[1])
        temp2 = nums[0]
        

        for i in range(2,len(nums)):
            curr = max(nums[i]+temp2, temp1)
            temp2 = temp1
            temp1 = curr

        return temp1
            


        # def dp_rob(n):
        #     if n<0:
        #         return 0
            
        #     if n==0:
        #         return nums[n]
            
        #     if dp_table[n]!=-1:
        #         return dp_table[n]
            
        #     pick =nums[n] + dp_rob(n-2)

        #     not_pick = dp_rob(n-1)

        #     return max(pick, not_pick)
        
        # return dp_rob(n-1)



        