class Solution:
    def isHappy(self, n: int) -> bool:
        
        # Happy Number is n=1 or n=7 otherwise False
        if n==1 or n==7:
            return True
    

        while n>9:
            num_str = str(n)
            digit_sum =0
            
            for char in num_str:
                digit_sum+= (int(char) * int(char))
            
            if digit_sum == 1 or digit_sum==7:
                return True
    
            n=digit_sum
        
        return False


            



        