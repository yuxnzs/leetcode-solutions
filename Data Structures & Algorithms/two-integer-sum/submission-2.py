class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, num in enumerate(nums):
            if num in seen:
                return [seen[num], i]

            complement = target - num
            seen[complement] = i

        return []