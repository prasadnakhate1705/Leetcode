class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t)>len(s):
            return ''

        if t == "":
            return ""

        count = Counter(t)
        have, need = 0, len(count)
        
        window = {}

        res = [-1,-1]
        res_len = float('inf')
        
        left = 0

        for right in range(len(s)):

            c =  s[right]
            window[c] = window.get(c, 0) + 1

            if c in window and window[c]==count[c]:
                have+=1
            
            while have==need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                window[s[left]] -= 1

                if s[left] in count and window[s[left]] < count[s[left]]:
                    have -= 1
                
                left+=1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""


            

            






        