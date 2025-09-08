import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)  ## storing the count
        maxheap = [[-cnt, char]for char, cnt in count.items()] ## -cnt for maxheap 
        heapq.heapify(maxheap)

        prev=None
        res =''

        while maxheap or prev:

            if prev and not maxheap:
                return ''
                
            #most frquent char except the prev
            cnt , char = heapq.heappop(maxheap)
            res+=char
            cnt+=1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None

            #adding the char baack to list if cnt not 0
            if cnt!=0:
                prev = [cnt, char]

        return res

                    
        
   
            
        