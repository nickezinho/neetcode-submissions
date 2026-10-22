class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        lines = len(grid)
        columns = len(grid[0])
        max_area = 0
      
        def maxArea(l, c):
            if (
                l < 0 or l >= lines 
                or c < 0 or c >= columns 
                or grid[l][c] == 0):
                return
  
            grid[l][c] = 0
           
            down = maxArea(l + 1, c) or 0
            up = maxArea(l - 1, c) or 0
            right = maxArea(l, c + 1) or 0
            left = maxArea(l, c - 1) or 0
            
            return 1 + (down + up + right + left)
            
        for l in range(lines):
            for c in range(columns):
                if grid[l][c] == 1:
                    max_area = max(max_area, maxArea(l, c))

        return max_area
