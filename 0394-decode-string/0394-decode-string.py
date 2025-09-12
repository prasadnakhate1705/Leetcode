class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        string= ''
        for i in range(len(s)):
            if s[i]==']':
                while stack[-1]!='[':
                    ch = stack.pop()
                    string = ch + string
                stack.pop()
                mul = stack.pop()
                string = int(mul)*string
                print(string)
                stack.append(string)
                string =''
                continue
            
            stack.append(s[i])
        
        return ''.join(stack)
        


             


            
            
        
        