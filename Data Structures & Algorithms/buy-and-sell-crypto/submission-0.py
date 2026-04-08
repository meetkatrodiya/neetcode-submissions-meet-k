class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        left = 0
        right = 1

        while left < right and right < len(prices) and left < len(prices):

            if prices[left] <= prices[right] :
                max_profit = max(max_profit , prices[right] - prices[left] )
                right += 1
            else:
                left = right
                right += 1

        return max_profit 
