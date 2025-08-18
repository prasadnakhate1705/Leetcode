class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        n = len(s)

        def palindrome(i):

            if i >= (n/2):
                return True
            
            if s[i] != s[n-i-1]:
                return False
            
            return  palindrome(i+1)
        
        return palindrome(0)
        