class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        dp = matrix[-1][:]
        temp = dp[:]
        n = len(matrix)

        for i in range(n-2, -1, -1):
            for j in range(n):
                if j==0:
                    dp[j] = matrix[i][j] + min(temp[j], temp[j+1])
                elif j==n-1:
                    dp[j] = matrix[i][j] + min(temp[j], temp[j-1])
                else:
                    dp[j] = matrix[i][j] + min(temp[j-1], temp[j], temp[j+1])

            temp = dp[:]
        
        return min(dp)



        
        