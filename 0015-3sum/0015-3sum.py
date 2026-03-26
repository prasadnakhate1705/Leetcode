class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        hash_map = {}
        nums.sort()
        ans = []

        for i in range(0,len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l=i+1
            r= len(nums)-1
            
            while(l<r):
                if nums[l] + nums[r] + nums[i]==0:
                    ans.append( [nums[l],nums[i],nums[r] ])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l+=1
                    r-=1
                elif nums[l] + nums[r] + nums[i] <0:
                    l+=1
                else:
                    r-=1
        
        return ans


        