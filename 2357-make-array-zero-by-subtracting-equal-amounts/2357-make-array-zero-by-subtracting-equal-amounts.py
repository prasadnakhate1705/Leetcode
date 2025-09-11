import heapq
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        nums.sort()
        count =0
        x = 0
        index =0

        if sum(nums)==0:
            return count

        for i in range(len(nums)):
            if nums[i]!=0:
                index=i
                break
        
        while index!= len(nums):
            x = nums[index]
            count+=1
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i]-=x
                
                if nums[i]==0:
                    index= i+1
            
            print(nums)

            
        
        return count
        
        

            

        




            
        