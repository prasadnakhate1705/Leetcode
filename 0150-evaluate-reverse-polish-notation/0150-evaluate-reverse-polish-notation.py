class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        # Map string operators to functions from the operator module
        OPERATIONS = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }

        i=0
        stack = []

        while i< len(tokens):

            if tokens[i] not in OPERATIONS:
                stack.append(int(tokens[i]))
            else:
                sec = stack.pop()
                first = stack.pop()

                res = OPERATIONS[tokens[i]](first,sec)
                stack.append(res)
            
            i+=1
        
        return stack[-1]
                
        