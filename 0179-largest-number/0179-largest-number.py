class Solution:
    def largestNumber(self, nums: List[int]) -> str:


        for i , n in enumerate(nums):
            nums[i] = str(n)

        n = len(nums)

        # bubble sort
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        # remove leading zeros
        res = ""
        for num in nums:
            res += num

        # handle case like "000"
        i = 0
        while i < len(res) - 1 and res[i] == '0':
            i += 1

        return res[i:]





        