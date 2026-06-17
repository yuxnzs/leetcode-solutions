class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先排序，讓 two pointers 可以根據總和大小移動，也讓重複值相鄰
        sorted_nums = sorted(nums)
        nums_length = len(sorted_nums)
        result = []

        previous_num = None
        for i in range(0, nums_length - 2):
            # 固定 current_num，剩下兩個數用 left / right 尋找
            left = i + 1
            right = nums_length - 1
            current_num = sorted_nums[i]

            # 跳過重複的 current_num，避免重複搜尋同一批組合
            if previous_num == current_num:
                continue
            previous_num = current_num

            while left < right:
                left_num = sorted_nums[left]
                right_num = sorted_nums[right]

                current_sum = current_num + left_num + right_num
                if current_sum < 0:
                    # 總和太小，left 往右讓數字變大
                    left += 1
                elif current_sum > 0:
                    # 總和太大，right 往左讓數字變小
                    right -= 1
                else:
                    result.append([current_num, left_num, right_num])

                    # 跳過連續重複的 left_num，避免產生重複組合
                    while left < right and left_num == sorted_nums[left + 1]:
                        left += 1

                    # 跳過連續重複的 right_num，避免產生重複組合
                    while left < right and right_num == sorted_nums[right - 1]:
                        right -= 1

                    # 離開目前這組答案，繼續在剩餘範圍找下一組
                    left += 1
                    right -= 1

        return result
        