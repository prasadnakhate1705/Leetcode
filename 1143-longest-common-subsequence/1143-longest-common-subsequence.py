class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # dp = {} ## DP dict to store the (i,j)->count

        # def LCS(i,j):
        #     if i<0 or j<0:
        #         return 0

        #     if (i,j) in dp:
        #         return dp[(i,j)]
            
        #     if text1[i]==text2[j]:
        #         #Match
        #         dp[(i,j)] =  1+ LCS(i-1, j-1)  
        #     else:
        #         #No Match
        #         # Max of two option. 
        #        dp[(i,j)] =  max(LCS(i-1,j), LCS(i,j-1))
               
        #     return dp[(i,j)] 

        # return LCS(n,m)

        ## Tabulation

        n = len(text1)
        m = len(text2)
        
        dp = [[0]* (m) for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    dp[i][j]= 1 + (dp[i-1][j-1] if i > 0 and j > 0 else 0)
                else:
                    dp[i][j] = max((dp[i-1][j] if i>0 else 0), (dp[i][j-1] if j>0 else 0))
            

        return dp[n-1][m-1]
        



            

            
        