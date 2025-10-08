class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jwl = set()
        for char in jewels:
            jwl.add(char)
        
        count=0

        for stone in stones:
            if stone in jwl:
                count+=1
        
        return count