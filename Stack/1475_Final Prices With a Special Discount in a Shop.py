from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        limit=len(prices)
        result_list=[]
        for i in range(limit):
            flag=0
            for j in range(i+1,limit):
                if(j>i and prices[j]<=prices[i]):
                    flag=1
                    result=prices[i]-prices[j]
                    result_list.append(result)
                    break
            if(flag==0):
                result_list.append(prices[i])
        
        return result_list
        
if __name__=="__main__":
    obj=Solution()
    prices = [8,4,6,2,3]
    result=obj.finalPrices(prices)
    print(result)