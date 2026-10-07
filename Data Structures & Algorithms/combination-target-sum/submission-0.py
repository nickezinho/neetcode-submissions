class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(inicio, caminho, total_atual):
            if total_atual == target:
                res.append(list(caminho))
                return
            if total_atual > target:
                return

            for i in range(inicio, len(nums)):
                caminho.append(nums[i])
                backtrack(i, caminho, total_atual + nums[i])
                caminho.pop()

        backtrack(0, [], 0)
        return res
