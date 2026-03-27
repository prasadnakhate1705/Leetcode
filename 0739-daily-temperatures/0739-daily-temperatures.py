class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        ans = [0]*len(temperatures)

        i = 0

        while i<len(temperatures):
            if not stack or temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
            else:
                while stack and (temperatures[stack[-1]]<temperatures[i]):
                    top = stack.pop()
                    ans[top]= i-top

                stack.append(i)
            i+=1
        
        return ans

        