from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=list()
        if matrix==[]:
            return result
        matrix_out_size=len(matrix)
        matrix_in_size=len(matrix[0])
        left=0
        right=matrix_in_size-1
        up=0
        down=matrix_out_size-1
        while(left<=right and up<=down):
            for i in range(left,right+1):
                result.append(matrix[up][i])
            up+=1
            for i in range(up,down+1):
                result.append(matrix[i][right])
            right-=1
            if(up> down or left >right):
                break
            for i in range(right,left-1,-1):
                result.append(matrix[down][i])
            down-=1
            for i in range(down,up-1,-1):
                result.append(matrix[i][left])
            left+=1
        return result
    
if __name__=="__main__":
    obj=Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result=obj.spiralOrder(matrix)
    print(result)