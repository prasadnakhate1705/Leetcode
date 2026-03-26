class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i,j = 0,0
        seen = set()
        max_size = 0
    
        while j<len(s) and i<len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i+=1
        
            seen.add(s[j])
            max_size = max(max_size, j-i+1)
            j+=1
        
        return max_size
            




        