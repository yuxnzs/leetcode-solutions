class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy_price = prices[0]
        sell_index = 1
        max_profit = 0

        while sell_index <= len(prices) - 1:
            sell_price = prices[sell_index]

            # 先用目前最低買入價計算今天賣出的利潤
            max_profit = max(max_profit, sell_price - lowest_buy_price)

            # 如果今天價格更低，更新目前最低買入價
            lowest_buy_price = min(lowest_buy_price, sell_price)

            sell_index += 1

        return max_profit
        