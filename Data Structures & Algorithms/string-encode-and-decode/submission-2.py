class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            # 固定格式：字串長度_字串內容
            result += str(len(s)) + "_" + s

        return result

    def decode(self, s: str) -> List[str]:
        result_list = []

        # 目前要解析的位置
        char_index = 0
        while char_index < len(s):
            # 從目前位置開始找 `_` 分隔符位置
            separator_index = char_index
            while s[separator_index] != "_":
                separator_index += 1

            # 取得目前這段字串的長度
            number_of_chars = int(s[char_index:separator_index])

            # 開始裁切的位置：`_` 後的第一位置
            string_start_index = separator_index + 1
            # 下一組資料的起點（結束裁切的位置）
            next_char_index = string_start_index + number_of_chars

            # 根據長度切出原本的字串
            result_list.append(s[string_start_index:next_char_index])

            # 移到下一組資料的起點
            char_index = next_char_index

        return result_list
        