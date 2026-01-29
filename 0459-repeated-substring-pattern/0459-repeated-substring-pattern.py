class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        double = s+s

        if s in double[1:-1]:
            return True
        
        return False

        
            
        
        
        

        