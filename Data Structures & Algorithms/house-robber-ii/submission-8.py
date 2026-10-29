class Solution:
    def rob_linear(self, nums):
        
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return nums[1]
        
        memo = {0:nums[0], 1:max(nums[0], nums[1])}
        def dfs(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i]+dfs(i-2), dfs(i-1))
                return memo[i]
        return dfs(n-1)
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        a = self.rob_linear(nums[:-1])
        b = self.rob_linear(nums[1:])
        
        return max(a,b)
        
        
            

            