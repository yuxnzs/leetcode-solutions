class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grouped_nums = dict(Counter(nums))

        # 建立 frequency bucket，index 代表出現次數
        # 最高頻率最多是 len(nums)，所以長度需要 len(nums) + 1
        frequency_buckets = [[] for _ in range(len(nums) + 1)]

        result = []

        # 將每個數字放到對應頻率的 bucket 裡
        for num, frequency in grouped_nums.items():
            frequency_buckets[frequency].append(num)

        # 從高頻率往低頻率掃，優先取出出現次數最多的數字
        for bucket in reversed(frequency_buckets):
            if bucket:
                result.extend(bucket)

        # 只回傳出現次數最高的前 k 個元素
        return result[:k]
        