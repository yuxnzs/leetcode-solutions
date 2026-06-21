class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_count = Counter()
        current_max_count = 0
        longest_count = 0

        for right, current_char in enumerate(s):
            char_count[current_char] += 1
            current_max_count = max(char_count.values())

            while right - left + 1 - current_max_count > k:
                char_count[s[left]] -= 1
                left += 1
                current_max_count = max(char_count.values())

            longest_count = max(longest_count, right - left + 1)

        return longest_count
        