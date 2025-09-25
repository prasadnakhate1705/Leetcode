class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n==1:
            return [0]
        
        ans = []

        

        for i in range(n//2):
            x = randint(1,100)
            ans.append(x)
            ans.append(-x)
        
        if n%2!=0:
            ans.append(0)
        
        return ans
        
        

            