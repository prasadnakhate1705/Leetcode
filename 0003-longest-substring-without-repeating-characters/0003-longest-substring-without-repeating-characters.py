class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        seen = set()
        max_size = 0
    
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
        
            seen.add(s[right])
            max_size = max(max_size, right-left+1)
        
        return max_size
            




        