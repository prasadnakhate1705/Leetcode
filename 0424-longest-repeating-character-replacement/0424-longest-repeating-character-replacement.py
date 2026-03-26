class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        max_freq = 0
        left = 0
        res =0

        for i in range(len(s)):

            if s[i] not in hash_map:
                hash_map[s[i]]=0
            hash_map[s[i]]+=1
            max_freq = max(max_freq, hash_map[s[i]])

            if (i-left+1)-max_freq >k:
                hash_map[s[left]]-=1
                left+=1
                
            
            res = max(res, i - left + 1)
        
        return res
            


       



        