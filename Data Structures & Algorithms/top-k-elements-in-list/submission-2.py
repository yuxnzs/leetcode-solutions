class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        num_heap = []

        # 計算每個數字出現次數
        for num in nums:
            num_count[num] += 1

        for num, count in num_count.items():
            # tuple 第一個值會作為 Heap 比較依據
            heapq.heappush(num_heap, (count, num))

            # 若超過 k，移除目前最小的
            if len(num_heap) > k:
                heapq.heappop(num_heap)

        return [num for count, num in num_heap]
        