"""
Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

# approach: dynamic programming
# memory: O(2n)
# runtime: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        days = len(prices)
        # special case: 0 - 1 days
        if days <= 1:
            return 0
        
        # special case: 2 days
        if days == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0
        
        # initialize our lookup matrix
        lm = []
        for day in range(days):
            lm.append([0,0])

        # lm[day][0] = best scenario if we didn't own stock on that day
        # lm[day][1] = best scenario if we owned stock on that day
        
        # lm[0][0] = 0                                           # price we paid to sideline
        # lm[0][1] = -prices[0]                                  # price we paid to enter
        # lm[1][0] = max(lm[0][0], lm[0][1] + prices[1])         # maximize sideling vs. buying/selling
        # lm[1][1] = max(lm[0][1], lm[0][0] - prices[1])         # minimize entry cost
        # for i in range(2, days):
        #     lm[i][0] = max(lm[i-1][0], lm[i-1][1] + prices[i]) # maximize sidelining vs. skin in the game, day by day
        #     lm[i][1] = max(lm[i-1][1], lm[i-2][0] - prices[i]) # minimize potential entries, accounting for cooldown
        
        lm[0][0] = 0                                           # price we paid to sideline
        lm[0][1] = prices[0]                                   # price we paid to enter
        lm[1][0] = max(lm[0][0], prices[1] - lm[0][1])         # maximize sideling vs. buying/selling
        lm[1][1] = min(lm[0][1], prices[1])                    # minimize entry cost
        for i in range(2, days):
            lm[i][0] = max(lm[i-1][0], prices[i] - lm[i-1][1]) # maximize sidelining vs. skin in the game, day by day
            lm[i][1] = min(lm[i-1][1], prices[i] - lm[i-2][0]) # minimize potential entries, accounting for cooldown
        
        # return the possibility where don't own stocks on the last trading day
        return lm[-1][0]
