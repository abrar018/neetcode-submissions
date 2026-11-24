class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=set(nums)
        if len(nums)==len(i):
            return False
        return True
