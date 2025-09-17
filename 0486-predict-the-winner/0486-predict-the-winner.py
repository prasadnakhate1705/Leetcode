class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def max_diff(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == j:
                return nums[i]
            
            # Player 1's optimal choice
            score1 = nums[i] - max_diff(i + 1, j)
            score2 = nums[j] - max_diff(i, j - 1)
            
            memo[(i, j)] = max(score1, score2)
            return memo[(i, j)]

        ans = max_diff(0, len(nums) - 1) >= 0

        return ans

                

                


        