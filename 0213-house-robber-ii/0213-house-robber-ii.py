class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def rob_linear(houses):
            prev2 = houses[0]
            prev1 = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                curr = max(houses[i] + prev2, prev1)
                prev2, prev1 = prev1, curr

            return prev1

        # Case 1: exclude last
        case1 = rob_linear(nums[:-1])
        # Case 2: exclude first
        case2 = rob_linear(nums[1:])

        return max(case1, case2)
