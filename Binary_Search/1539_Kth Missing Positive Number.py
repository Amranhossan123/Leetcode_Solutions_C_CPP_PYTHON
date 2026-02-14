from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        result_list=list()
        for i in range(1,2001):
            if i not in arr:
                result_list.append(i)
        return result_list[k-1]
    
if __name__=="__main__":
    obj=Solution()
    arr = [1,2,3,4]
    k = 2
    result=obj.findKthPositive(arr,k)
    print(result)
    
        