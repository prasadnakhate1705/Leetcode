class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n=len(word1)
        m = len(word2)

        dp_Dict = {}

        def LCS(i,j):
            if i<0 or j<0:
                return 0
            
            if (i,j) in dp_Dict:
                return dp_Dict[(i,j)]
            
            if word1[i]==word2[j]:
                dp_Dict[(i,j)]= 1+ LCS(i-1, j-1)
            else:
                dp_Dict[(i,j)] = max(LCS(i,j-1), LCS(i-1, j))
            
            return dp_Dict[(i,j)]
        
        lcs = LCS(n-1,m-1)

        ans = (n-lcs) + (m-lcs)


        return ans
            

        