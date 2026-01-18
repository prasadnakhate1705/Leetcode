class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()
        s = s.split(" ")
        s.reverse()
        res = ''

        for word in s:
            if word!='':
                res = res + ' '+  word 

        return res.strip()
        




        