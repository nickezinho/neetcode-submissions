class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        lines = len(grid)
        columns = len(grid[0])

        total_islands = 0

        def islands(l, c):
            if (
                l < 0 
                or l >= lines 
                or c < 0 
                or c >= columns 
                or grid[l][c] == '0'):
                return

            grid[l][c] = '0'

            islands(l + 1, c)
            islands(l - 1, c)
            islands(l, c + 1)
            islands(l, c - 1)
        
        for l in range(lines):
            for c in range(columns):
                if grid[l][c] == '1':
                    total_islands += 1
                    islands(l, c)

        return total_islands