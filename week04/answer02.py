# solution1
def maxProfit(prices):
    max_profit = 0
    
    for i in range(len(prices)-1):
        for j in range(i, len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                
                if profit > max_profit:
                    max_profit = profit
    
    return max_profit

# solution2
def maxProfit2(prices):
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        if price < min_price:
            min_price = price
            
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        
    return max_profit
