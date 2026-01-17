class Solution:
    def bestClosingTime(self, customers: str) -> int:

        penalty = customers.count('N')

        min_penalty = penalty
        res = 0

        for i,c in enumerate(customers):
            if c == 'Y':
                penalty-=1
            else:
                penalty+=1

            if penalty<min_penalty:
                min_penalty = penalty
                res = i+1

        return res 
        

        




        