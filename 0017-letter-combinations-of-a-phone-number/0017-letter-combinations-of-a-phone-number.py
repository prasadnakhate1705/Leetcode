class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hash_map = {'2':['a','b','c'], '3':['d','e','f'], '4': ['g','h','i'], '5':['j','k','l'],
                    '6':['m','n','o'], '7':['p','q','r', 's'], '8':['t','u','v'], '9':['w','x','y','z']}
        
        
        if len(digits)==0:
            return []
        
        Output = []

        def back_track(index, curr_string):
            if len(curr_string)==len(digits):
                Output.append(curr_string)
                return 
            
            for letter in hash_map[digits[index]]:
                back_track(index+1, curr_string+ letter)
        
        back_track(0,'')

        return Output


        


            

        

        