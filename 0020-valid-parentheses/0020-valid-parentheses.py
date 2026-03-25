class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        hash_map = {')':'(','}':'{',']':'['}

        for char in s:

            if not stack:
                stack.append(char)
                continue

            if stack:
                if char==')' and stack[-1]==hash_map[char]:
                    stack.pop()
                elif char=='}' and stack[-1]==hash_map[char]:
                    stack.pop()
                elif char==']' and stack[-1]==hash_map[char]:
                    stack.pop()
                else:
                    stack.append(char)
            
            
        
        if len(stack)>0:
            return False
        else:
            return True

        

        