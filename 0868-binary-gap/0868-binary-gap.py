class Solution:
    def binaryGap(self, n: int) -> int:
        binary = format(n, 'b')

        
        idx = []

        for i in range(len(binary)):
            if binary[i]=='1':
                idx.append(i)
        
        ans = 0

        for i in range(len(idx)-1):
            ans = max(ans, (idx[i+1]-idx[i]))
        
        
        return ans
                
                
                
                
