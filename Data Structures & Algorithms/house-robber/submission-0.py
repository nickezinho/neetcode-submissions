class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)

        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])

        # memo = {0:nums[0], 1:max(nums[0], nums[1])}
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = max(nums[i]+dfs(i-2), dfs(i-1))
        #         return memo[i]
        # return dfs(n-1)

        # I prefer tabulation, is a lot easier.

        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):

            prev, curr = curr, max(nums[i] + prev, curr)
        
        return curr
            
        