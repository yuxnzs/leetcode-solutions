class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            # unescape 跳脫字元
            escaped_string = s.encode("unicode_escape").decode()
            result += str(len(escaped_string)) + "_" + escaped_string

        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        result_list = []

        char_index = 0
        while True:
            # 獲取下個字長度
            number_of_chars = 0
            num_string = ""
            for index, _ in enumerate(s):
                num_string += s[char_index + index]

                if s[char_index + index + 1] == "_":
                    number_of_chars += int(num_string)
                    break

            # 計算下次指向長度位置的字元位置
            next_char_index = (
                char_index + number_of_chars + 1 + len(str(number_of_chars))
            )
            result_list.append(
                s[char_index + 1 + len(str(number_of_chars)) : next_char_index]
                .encode()
                .decode("unicode_escape")
            )  # 裁切後加入陣列
            char_index = next_char_index

            if char_index + 1 > len(s):
                break

        return result_list
