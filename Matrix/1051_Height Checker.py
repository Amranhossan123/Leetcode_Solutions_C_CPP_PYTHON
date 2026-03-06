from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=heights.copy()
        expected.sort()
        total=0
        limit=len(heights)
        for i in range(limit):
            if heights[i] != expected[i]:
                total+=1
        return total
        
        
if __name__=="__main__":
    obj=Solution()
    heights = [1,1,4,2,1,3]
    result=obj.heightChecker(heights)
    print(result)