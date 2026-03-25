class Solution:
    def isPalindrome(self, x: int) -> bool:

        rev = 0
        original = x

        while original>0:
            temp = original%10
            rev = temp + (10* rev)
            original = original//10
        
        return rev==x