from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        limit=len(nums)
        increase=True
        decrease=True
        for i in range(limit-1):
            if(nums[i]>nums[i+1]):
                decrease=False
            if(nums[i] < nums[i+1]):
                increase=False
        return increase or decrease
if __name__=="__main__":
    obj=Solution()
    nums = [1,2,2,3]
    result=obj.isMonotonic(nums)
    print(result)
           
                


        