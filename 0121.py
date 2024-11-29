class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i, j = 0, 0
        max_profit = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                cur_profit = prices[j] - prices[i]
                max_profit = max(max_profit, cur_profit)
            else:  # update i when find lower price
                i = j
            j += 1
        return max_profit


s = Solution()
tests = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1],
]
for test in tests:
    print(s.maxProfit(test))
