class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        res = 0
        seen = set()

        while k>0:
            max_val = float('-inf')
            idx =0

            for i, num in enumerate(happiness):
                if num > max_val and i not in seen:
                    max_val = num
                    idx = i
                
                if happiness[i]>0:
                    happiness[i]-=1
            
            res+=max_val
            seen.add(idx)
            k-=1
        
        return res

        