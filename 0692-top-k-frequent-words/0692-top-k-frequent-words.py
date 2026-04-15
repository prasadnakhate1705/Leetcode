class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = {}
        # hash_map
        for i in range(len(words)):
            if words[i] not in count:
                count[words[i]]=0
            count[words[i]]+=1
        
        res = []
        for i, (key, value) in enumerate(count.items()):
            res.append((key, value))
        
        for i in range(len(res)):
            for j in range(0, len(res) - i - 1):
                if res[j][1] < res[j+1][1] or \
                   (res[j][1] == res[j+1][1] and res[j][0] > res[j+1][0]):
                    res[j], res[j+1] = res[j+1], res[j]
                

        ans = []

        for i in range(k):
            ans.append(res[i][0])

        return ans
            

        