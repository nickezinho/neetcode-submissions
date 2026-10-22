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
                return 0
  
            grid[l][c] = 0
           
            return 1 + (
                maxArea(l + 1, c) + 
                maxArea(l - 1, c) +
                maxArea(l, c + 1) +
                maxArea(l, c - 1) 
          
            )
  
        for l in range(lines):
            for c in range(columns):
                if grid[l][c] == 1:
                    max_area = max(max_area, maxArea(l, c))

        return max_area
