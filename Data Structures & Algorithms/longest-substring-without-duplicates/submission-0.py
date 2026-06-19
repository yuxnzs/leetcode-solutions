class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_count = 0
        current_str = set()  # 目前 window 內的字元

        for right in range(len(s)):
            current_char = s[right]

            # 檢查 current_char 是否已存在於目前 window
            # 若已存在，移除左側字元，直到 current_char 不再重複
            while current_char in current_str:
                current_str.remove(s[left])
                left += 1

            # 加入不重複的字元
            current_str.add(current_char)
            current_count = right - left + 1
            longest_count = max(longest_count, current_count)

        return longest_count
