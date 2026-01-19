class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        min_abs_val = float('inf')
        abs_sum = 0
        neg = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                abs_sum += abs(matrix[i][j])
                if matrix[i][j]<0:
                    neg+=1
                min_abs_val =  min(min_abs_val, abs(matrix[i][j]))


        if neg%2!=0:
            abs_sum -= 2* min_abs_val
        
        return abs_sum



        