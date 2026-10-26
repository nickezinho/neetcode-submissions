class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        q = deque()

        def bfs(q):
            while q:
                i, j = q.popleft()

                for dI, dJ in [(0, 1), (1, 0), (-1, 0), (0, -1)]:

                    r, c = i + dI, j + dJ
                    if 0 <= r < m and 0 <= c < n:
                        if board[r][c] == 'O':
                            board[r][c] = 'S'
                            q.append((r,c))
            

        for j in range(n):
            if board[0][j] == "O":
                board[0][j] = 'S'
                q.append((0,j))
                bfs(q)

        for j in range(n):
            if board[m - 1][j] == "O":
                board[m - 1][j] = 'S'
                q.append((m-1,j))
                bfs(q)

        for i in range(m):
            if board[i][0] == "O":
                board[i][0] = 'S'
                q.append((i,0))
                bfs(q)

        for i in range(m):
            if board[i][n - 1] == "O":
                board[i][n - 1] = 'S'
                q.append((i,n-1))
                bfs(q)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'S':
                    board[r][c] = 'O'

        