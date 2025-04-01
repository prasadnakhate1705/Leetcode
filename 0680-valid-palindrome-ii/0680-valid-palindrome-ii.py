class Solution:
    def validPalindrome(self, s: str) -> bool:

        i,j = 0, len(s)-1

        while i<j:
            
            ## if not matching try skiping left or right character
            if s[i]!=s[j]:
                skipL, skipR = s[i+1:j+1], s[i:j]

                ## checking if the skipped part is palindrome
                return (skipL == skipL[::-1]) or (skipR==skipR[::-1])

            i+=1
            j-=1

        ## else return true
        return True        
            
             
        