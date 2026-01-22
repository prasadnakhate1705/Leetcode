class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = {}

        # hash_map
        for i in range(len(words)):
            if words[i] not in count:
                count[words[i]]=0
            count[words[i]]+=1
        
        
        res = []

        for i, (key,val) in enumerate(count.items()):
            if len(res)<k:
                heapq.heappush(res,(val,key))
                continue
            
            if res[0][0] < val:
                heapq.heappop(res)
                heapq.heappush(res,(val,key))
        
        
        ans =[]

        for i in range(k):
            ans.append(res[i][1])

        return ans.sort()
            

        