class Solution:
    # 0613 改進版：以先儲存、後更新簡化左右累積乘積的邊界處理
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        left_products = []
        result = [1] * nums_length

        # 算每個 index 左邊所有數字的乘積
        current_product = 1
        for i in range(nums_length):
            left_products.append(current_product)
            current_product *= nums[i]

        # 從右往左算右邊乘積，並合併左邊乘積
        current_product = 1
        for i in range(nums_length - 1, -1, -1):
            result[i] = left_products[i] * current_product
            current_product *= nums[i]

        return result
        