from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        dead = set(deadends)

        if '0000' in dead:
            return -1
        
        if target == "0000":
            return 0

        queue = deque([('0000',0)])
        visited = set("0000")

        while queue:
            combination, steps = queue.popleft()

            for i in range(4):
                digit= int(combination[i])

                for move in[1,-1]:
                    new_digit = (digit + move) % 10
                    new_comb = combination[:i] + str(new_digit) + combination[i+1:]

                    if new_comb == target:
                        return steps + 1

                    if new_comb not in visited and new_comb not in dead:
                        queue.append((new_comb, steps + 1))
                        visited.add(new_comb)        

        return -1

