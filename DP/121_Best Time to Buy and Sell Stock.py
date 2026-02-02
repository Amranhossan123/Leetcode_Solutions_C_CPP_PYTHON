from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') 
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            
            profit = price - min_price
            max_profit = max(max_profit, profit)
            
        return max_profit
    
if __name__=="__main__":
    obj=Solution()
    prices = [7,1,5,3,6,4]
    result=obj.maxProfit(prices)
    print(result)