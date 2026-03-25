class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        ans = []
        n = len(nums)
        nums = set(nums)

        for i in range(1, n+1):

            if i not in nums:
                print(i)
                ans.append(i)

        return ans        