class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        ans, sol = [], []

        mapping = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        n = len(digits)

        def dfs(i=0):
            if i == n:
                ans.append(''.join(sol))
                return

            for letter in mapping[digits[i]]:
                sol.append(letter)
                dfs(i+1)
                sol.pop()

        dfs()
        return ans

