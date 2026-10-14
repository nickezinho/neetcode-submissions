class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res, subsets = [], []

        def dfs(i):
            if i >= len(nums):
                if subsets not in res:
                    res.append(subsets[:])
                return
            
            subsets.append(nums[i])
            dfs(i + 1)

            subsets.pop()
            dfs(i + 1)

        dfs(0)
        return res