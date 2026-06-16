class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 移除非英文字母與數字
        cleaned_string = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        left = 0
        right = len(cleaned_string) - 1

        while left < right:
            if cleaned_string[left] != cleaned_string[right]:
                return False

            left += 1
            right -= 1

        return True
        