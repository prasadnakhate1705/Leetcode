class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        target = sum(nums)//2
        dp = [[-1]*(target+1) for _ in range(n)]

        if sum(nums)%2==1:
            return False


        def func(i, target):
            if target==0:
                return True
            
            if i==0:
                return (nums[0]==target)
            
            if dp[i][target]!=-1:
                return dp[i][target]
            
            not_take = func(i-1, target)
            take = False

            if nums[i]<=target:
                take = func(i-1, target-nums[i])
            
            dp[i][target]= take or not_take

            return dp[i][target]
        
        return func(n-1,target)


        # total = sum(nums)
        # if total % 2 ==1:
        #     return False
        
        # target = total//2

        # # DP array
        # dp = [False] * (target + 1)

        # dp[0] = True

        # for num in nums:
        #     for t in range(target, num-1, -1):
        #         dp[t] = dp[t] or dp[t-num]
        
        # return dp[target]




        



        