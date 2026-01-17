class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        
        res = []
        depth = 0

        for i in range(len(s)):

            if s[i]=='(':
                if depth>0:
                    res.append(s[i])
                depth+=1
            else:
                depth-=1
                if depth>0:
                    res.append(s[i])

             
        return ''.join(res)