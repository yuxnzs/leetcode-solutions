from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [0 for _ in range(len(nums))]
        result = [0 for _ in range(len(nums))]

        l_product = 1
        for i in range(len(nums)):
            # 儲存目前 index 左邊所有數字的 product（不包含自己）
            left_products[i] = l_product

            # 更新 product 提供給下一個 index 使用
            l_product *= nums[i]

        r_product = 1
        for i in range(len(left_products) - 1, -1, -1):
            # 左邊 product * 右邊 product
            result[i] = left_products[i] * r_product

            # 更新右邊 product，提供給下一個 index 使用
            r_product *= nums[i]

        return result
