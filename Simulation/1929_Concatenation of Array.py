from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums=nums
        result_list=new_nums+nums
        return result_list
    
if __name__=="__main__":
    obj=Solution()
    nums = [1,2,1]
    result=obj.getConcatenation(nums)
    print(result)
        