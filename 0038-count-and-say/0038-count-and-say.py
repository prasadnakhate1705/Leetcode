class Solution:
    def countAndSay(self, n: int) -> str:

        res = ['1']

        if n==1:
            return ''.join(res)
        
        def helper(res):
            newstr = []
            count=1

            for i in range(len(res)-1):
                if res[i]==res[i+1]:
                    count+=1
                
                elif res[i]!=res[i+1]:
                    newstr.append(str(count))
                    newstr.append(str(res[i]))
                    count=1
            
            newstr.append(str(count))
            newstr.append(str(res[-1]))
                
            return newstr


        for _ in range(2,n+1):
            res = helper(res)
        
        return ''.join(res) 
            
            



        