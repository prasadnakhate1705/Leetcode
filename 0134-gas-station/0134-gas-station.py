class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        if sum(gas) < sum(cost):
            return -1

        start_station = 0
        current_gas = 0
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            
            if current_gas < 0:
                start_station = i + 1
                current_gas = 0
                
        return start_station
        
        

        
        

            
        