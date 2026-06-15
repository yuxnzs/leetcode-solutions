class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_nums = set(nums)
        sequence_start_candidates = set()
        longest_length = 0

        # 找出每段序列的起點
        for unique_n in unique_nums:
            if unique_n - 1 not in unique_nums:
                sequence_start_candidates.add(unique_n)

        # 從每個起點往後計算連續長度，並更新最大值
        for candidate in sequence_start_candidates:
            current_length = 1
            next_number = candidate + 1

            while next_number in unique_nums:
                current_length += 1
                next_number += 1

            longest_length = max(longest_length, current_length)

        return longest_length
        