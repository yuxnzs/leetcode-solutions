class Solution:
    # 0618 改進版
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy_price = prices[0]
        max_profit = 0

        for sell_price in prices[1:]:
            max_profit = max(max_profit, sell_price - lowest_buy_price)
            lowest_buy_price = min(lowest_buy_price, sell_price)

        return max_profit
