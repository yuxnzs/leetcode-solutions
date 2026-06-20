class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_count = Counter()
        max_char_count = 0
        longest_count = 0

        for right, current_char in enumerate(s):
            char_count[current_char] += 1
            max_char_count = max(char_count.values())

            # 若目前 window 需要替換的字元數超過 k，持續縮小左邊界直到 window 合法
            while right - left + 1 - max_char_count > k:
                char_count[s[left]] -= 1
                left += 1
                max_char_count = max(char_count.values())

            longest_count = max(longest_count, right - left + 1)

        return longest_count
