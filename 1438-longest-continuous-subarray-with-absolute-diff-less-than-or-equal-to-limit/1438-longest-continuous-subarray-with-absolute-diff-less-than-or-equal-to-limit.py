class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        maxdq = deque()
        mindq = deque()

        res = 0
        l=0

        for r in range(len(nums)):

            while maxdq and maxdq[-1]<nums[r]:
                maxdq.pop()
            maxdq.append(nums[r])

            while mindq and mindq[-1]>nums[r]:
                mindq.pop()
            mindq.append(nums[r])

            if abs(maxdq[0]-mindq[0])>limit:

                if nums[l]==maxdq[0]:
                    maxdq.popleft()
                
                if nums[l]==mindq[0]:
                    mindq.popleft()
                
                l+=1
            
            res = max(res, r-l+1)

        return res

        # small ,large = float('inf'),0
        # l,r = 0,0
        
        # res = 0

        # while(l<len(nums) and r<len(nums)):
        #     small = min(small,nums[r])
        #     large = max(large, nums[r])

        #     if abs(large-small)<=limit:
        #         res = max(res, r-l+1)
        #     elif abs(large-small)>limit:
        #         l+=1
        #         r = l
        #         small,large = float('inf'), 0
        #         continue
                
        #     if r==len(nums)-1:
        #         l+=1
        #         r = l
        #         small,large = float('inf'), 0

        #     r+=1
        
        #return res





        
                
                
                



        

        