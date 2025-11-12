class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = {}

        n = len(text1)-1
        m = len(text2)-1

        def LCS(i,j):
            if i<0 or j<0:
                return 0

            if (i,j) in dp:
                return dp[(i,j)]
            
            if text1[i]==text2[j]:
                dp[(i,j)] =  1+ LCS(i-1, j-1)
            else:
               dp[(i,j)] =  max(LCS(i-1,j), LCS(i,j-1))
            
            return dp[(i,j)] 

        return LCS(n,m)
        



            

            
        