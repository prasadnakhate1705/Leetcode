class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        temp= ''
        current_num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                current_num = 10* current_num + int(s[i])
            
            elif s[i]=='[':
                stack.append(current_num)
                stack.append(temp)
                temp = ''
                current_num = 0
            
            elif s[i] == ']':
                prev_string = stack.pop()
                num = stack.pop()
                temp = prev_string + num * temp
                current_num=0
            else:
                temp+=s[i]
        
        return temp


                

                
        return ''.join(stack)
        


             


            
            
        
        