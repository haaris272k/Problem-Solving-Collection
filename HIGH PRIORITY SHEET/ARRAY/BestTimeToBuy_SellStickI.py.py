"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell."""

# prices = [2, 1, 2, 0, 1]
prices = [7, 1, 5, 3, 6, 4]
prices = [1, 2, 3, 4, 5]
# Approach 1: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
maxProfit = []
for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        profit = prices[j] - prices[i]
        maxProfit.append(profit)
print(max(maxProfit))


# Approach 2: Two pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
ans = 0

# taking two pointers low and high
# low marks the start of the buy and high marks the end of the sell
low, high = 0, 1

while high < len(prices):

    # If the price is going down, we buy at the lowest price and sell at the highest price
    if prices[low] < prices[high]:
        ans = max(ans, prices[high] - prices[low])
        high += 1

    # If the price is going up, we buy at the lowest price and sell at the highest price
    # We also update the low pointer to the current high pointer
    # This is because we want to buy at the lowest price and sell at the highest price
    # If we don't update the low pointer, we will be buying at the highest price and selling at the highest price
    # which is not what we want
    # We also update the high pointer to the next index
    else:
        low = high
        high += 1
print(ans)
