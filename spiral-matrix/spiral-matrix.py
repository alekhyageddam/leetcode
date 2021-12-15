class Solution:
    #Algorithm: Given that we are at (row, col), where row is the row index, and col is the column index.
                # move right: (row, col + 1)
                # move downwards: (row + 1, col)
                # move left: (row, col - 1)
                # move upwards: (row - 1, col)
    #Approach: Setting up and adjusting matrix boundaries
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        
        up = left = 0
        right = columns - 1
        down = rows - 1
        
        while len(result) < rows * columns:
            #traverse from left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])
            
            #traverse downwards
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])
            
            #add check 1 to make sure we are traversing a different row
            if up != down:
                #traverse right to left
                for col in range(right - 1, left -1, -1):
                    result.append(matrix[down][col])
            
            
            #add check 1 to make sure we are traversing a different column
            if left != right:
                # traverse upwards    
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])
            
            left += 1
            right -= 1
            up += 1
            down -=1
        
        return result