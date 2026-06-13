class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        left_products = []
        result = []

        # 算每個 index 左邊所有數字的乘積
        current_product = 1
        for i in range(nums_length):
            if i == 0:
                left_products.append(1)
                continue

            left_product = current_product * nums[i - 1]
            left_products.append(left_product)
            current_product = left_product

        # 從右往左算右邊乘積，並合併左邊乘積
        current_product = 1
        previous_right_product = 1
        for i in range(nums_length - 1, -1, -1):
            if i == nums_length - 1:
                result.append(left_products[i])
                continue

            current_product = nums[i + 1] * previous_right_product
            right_product = left_products[i] * current_product
            result.append(right_product)
            previous_right_product = current_product

        return result[::-1]
        