class Solution:
    def alternateDigitSum(self, n: int) -> int:

        res =0
        pos = True
        digits = []

        while(n!=0):
            dig = n%10
            digits.append(dig)
            n = n//10
        
        for i in range(len(digits)-1,-1,-1):
            if pos:
                res+=digits[i]
                pos = False
            else:
                res+= (-digits[i])
                pos=True

        return res

        