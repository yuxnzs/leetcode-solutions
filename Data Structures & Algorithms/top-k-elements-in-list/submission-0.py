class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1

        sorted_list = []
        for key, _ in sorted(num_count.items(), key=lambda item: item[1], reverse=True):
            sorted_list.append(key)

        return sorted_list[:k]
        