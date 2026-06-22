class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for char in s:
            # 遇到右括號時，檢查 stack 最上面的左括號是否能配對
            if stack and char in pairs:
                if pairs[char] != stack[-1]:
                    return False
                else:
                    # 配對成功，移除最上面的左括號
                    stack.pop()
                    continue

            stack.append(char)

        # stack 清空代表所有括號都有成功配對
        return len(stack) == 0
