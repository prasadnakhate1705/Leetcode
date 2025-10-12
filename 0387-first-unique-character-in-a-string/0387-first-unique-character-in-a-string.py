class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count_dict = {}

        for char in s:
            if char not in count_dict:
                count_dict[char]=1
            else:
                count_dict[char]+=1
        
        for i,char in enumerate(s):
            if count_dict[char]==1:
                return i
        
        return -1
