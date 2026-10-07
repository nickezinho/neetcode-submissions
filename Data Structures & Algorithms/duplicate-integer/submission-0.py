class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = []

        for n in nums:
            if n in nums1:
                return True
            else:
                nums1.append(n)
        return False

        