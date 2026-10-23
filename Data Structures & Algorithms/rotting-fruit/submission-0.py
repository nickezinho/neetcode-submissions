class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = -1

        while q:
            q_size = len(q)
            minutes += 1

            for _ in range(q_size):
                row, col = q.popleft()
                for r, c in [(row, col +1), (row +1, col), (row, col -1),(row -1, col)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))
            
        if fresh == 0:
            return minutes
        else:
            return -1

                