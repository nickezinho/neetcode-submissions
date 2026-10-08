class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def dfs(op, cl):
            if len(sol) == 2*n:
                res.append(''.join(sol))
                return

            if op < n:
                sol.append('(')
                dfs(op + 1, cl)
                sol.pop()

            if op > cl:
                sol.append(')')
                dfs(op, cl +1)
                sol.pop()
        dfs(0,0)
        return res 
            