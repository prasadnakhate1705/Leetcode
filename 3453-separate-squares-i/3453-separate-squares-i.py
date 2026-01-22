class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        
        total_area = 0
        high = float('-inf')
        low = float('inf')

        for x,y, l in squares:
            total_area+=l*l
            high = max(high, y+l)
            low = min(low, y)
        

        def area_below(h):

            area =0

            for x, y, l in squares:

                if h>=y+l:
                    area+=l*l
                elif h>y and h<y+l:
                    area+=(h-y)*l
                else:
                    continue
            
            return area
        

        for _ in range(70):
            mid = (low+high)/2

            if area_below(mid)<total_area/2:
                low = mid
            else:
                high=mid
        
        return low
            

                    

        
        
        