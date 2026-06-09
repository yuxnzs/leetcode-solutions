class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        num_list = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            num_count[num] += 1

        for num, count in num_count.items():
            num_list[count].append(num)

        result_list = []
        for item in reversed(num_list):
            if item and len(result_list) < k:
                result_list.extend(item)

        return result_list[:k]
        