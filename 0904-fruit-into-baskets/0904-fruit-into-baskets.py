class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        fruits_count = defaultdict(int)
        left =0
        max_fruit = 0

        for right, fruit in enumerate(fruits):

            fruits_count[fruit]+=1 

            while len(fruits_count)>2:
                left_fruit = fruits[left]
                fruits_count[left_fruit] -= 1
                if fruits_count[left_fruit] == 0:
                    del fruits_count[left_fruit]
                left+=1

            max_fruit = max(max_fruit, right-left+1)       

        return max_fruit   
            

        