class Solution:
    def minInsertions(self, s: str) -> int:


        n = len(s)
        rs = s[::-1]

        dp_array = {}

        def LPS(i,j):
            if i<0 or j<0:
                return 0
            
            if (i,j) in dp_array:
                return dp_array[(i,j)]
            
            if s[i]==rs[j]:
                dp_array[(i,j)] = 1+ LPS(i-1,j-1)
            else:
                dp_array[(i,j)] = max(LPS(i,j-1), LPS(i-1,j))
            
            return dp_array[(i,j)]
        
        lps = LPS(n-1, n-1)

        return n-lps
        
        