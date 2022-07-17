class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        order = len(mat[0])
        diagonalSum = 0
        
        if order == 1:
            return mat[0][0]
        
        for i in range(order):
            
            diagonalSum += mat[i][i] + mat[i][order - i - 1]
            
        if order % 2 == 1:
            
            diagonalSum -= mat[order // 2][order//2]
            
            
        return diagonalSum
            