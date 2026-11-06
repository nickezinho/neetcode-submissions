class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            cLen = 1

            for idx in range(i + 1, len(nums)):
                if nums[idx] > nums[i]:
                    pathLen = 1 + dfs(idx)
                    cLen = max(cLen, pathLen)
            memo[i] = cLen
            return cLen
        
        return max(dfs(i) for i in range(len(nums)))
        
            
            