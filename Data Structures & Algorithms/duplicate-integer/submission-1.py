class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num = set()

        for n in nums:
            unique_num.add(n)

        return len(nums) != len(unique_num)
