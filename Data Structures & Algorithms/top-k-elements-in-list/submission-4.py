class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grouped_nums = Counter(nums)
        top_k_nums = [[] for _ in range(len(nums) + 1)]
        result = []

        for num, frequency in grouped_nums.items():
            top_k_nums[frequency].append(num)

        for num_arr in reversed(top_k_nums):
            if num_arr:
                result.extend(num_arr)

        return result[:k]
        