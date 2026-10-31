class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, max_product, min_product = nums[0],nums[0],nums[0]
        
        if len(nums) <= 1:
            return res

        for n in nums[1:]:
            temp_max = max_product
            temp_min = min_product

            max_product = max(n, n * temp_max, n * temp_min)
            min_product = min(n, n * temp_max, n * temp_min)
            res = max(res, max_product)

        return res
        
