class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp_table = [[-1]*(m+1) for _ in range(n+1)]

        # def dp(i,j):
        #     if i == 0:
        #         return j  # all inserts
        #     if j == 0:
        #         return i  #all inserts
            
        #     if dp_table[i][j]!= -1:
        #         return dp_table[i][j]
            
        #     if word1[i-1]==word2[j-1]:
        #         return dp(i-1,j-1)
        #     else:
        #         dp_table[i][j]= 1+ min(dp(i-1, j), dp(i,j-1), dp(i-1,j-1))
        #         return dp_table[i][j]
        

        # return dp(n,m)


        # Tabulation

        for i in range(n+1):
            dp_table[i][0] = i
        for j in range(m+1):
            dp_table[0][j] = j

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp_table[i][j]= dp_table[i-1][j-1]
                else:
                    dp_table[i][j] = 1 + min(dp_table[i-1][j] ,dp_table[i][j-1],dp_table[i-1][j-1])
        
        return dp_table[n][m]


        

         
            
             
                
            
            
            

            
        