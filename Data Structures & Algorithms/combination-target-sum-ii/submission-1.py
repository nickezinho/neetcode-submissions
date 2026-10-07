class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        nums = sorted(candidates)
        n = len(nums)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            for idx in range(i, n):
                if idx > i and nums[idx] == nums[idx -1]:
                    continue

                sol.append(nums[idx])
                backtrack(idx + 1, cur_sum + nums[idx])
                sol.pop()

        backtrack(0, 0)
        return res