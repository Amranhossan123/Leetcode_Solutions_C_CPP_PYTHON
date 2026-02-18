from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=list()
        limit=len(nums)
        for i in range(limit):
            target.insert(index[i],nums[i])
        return target


if __name__=="__main__":
    obj=Solution()
    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    result=obj.createTargetArray(nums,index)
    print(result)