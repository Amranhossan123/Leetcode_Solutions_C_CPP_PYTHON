from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        row=len(grid)
        colum=len(grid[0])
        for i in range(row):
            for j in range(colum):
                if grid[i][j]<0:
                    count+=1
        return count
    
if __name__=="__main__":
    obj=Solution()
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    result=obj.countNegatives(grid)
    print(result)
        