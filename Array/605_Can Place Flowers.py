from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        limit = len(flowerbed)
        
        for i in range(limit):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == limit - 1) or (flowerbed[i + 1] == 0)
            
                if left_empty and right_empty:
                    flowerbed[i] = 1 
                    count += 1
                    
        return count >= n
    
if __name__=="__main__"    :
    sol=Solution()
    flowerbed = [1,0,0,0,1] 
    n = 1
    result=sol.canPlaceFlowers(flowerbed,n)
    print(result)