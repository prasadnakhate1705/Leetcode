class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if stack:
                if s[i]==')'and stack[-1]=='(':
                    stack.pop()
                elif s[i]=='}'and stack[-1]=='{':
                    stack.pop()
                elif s[i]==']'and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(s[i])

            else:
                stack.append(s[i])
        
        return not stack
        