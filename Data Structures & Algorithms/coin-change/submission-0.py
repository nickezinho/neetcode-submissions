class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = float('inf')

        if amount == 0:
            return 0

        memo = {}

        def dfs(change):
            res = float("inf")

            if change == 0:
                return 0
                
            if change in memo:
                return memo[change]

            for coin in coins:
                new_change = change - coin 
                
                if new_change >= 0:
                    res = min(res, 1 + dfs(new_change))
            memo[change] = res
            return memo[change]

        result = dfs(amount)

        if result == float('inf'):
            return -1
        
        return result

                





