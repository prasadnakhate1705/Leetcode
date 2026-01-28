class Solution:
    def binaryGap(self, n: int) -> int:
        binary = format(n, 'b')

        
        ans = 0
        last = len(binary)

        for i in range(len(binary)-1, -1,-1):

            if binary[i]=='1':
                if last == len(binary):
                    last=i
                    continue
                
                if last!='1':
                    ans = max(ans, last-i)
                    last = i
                
        return ans
                
                
                
                
