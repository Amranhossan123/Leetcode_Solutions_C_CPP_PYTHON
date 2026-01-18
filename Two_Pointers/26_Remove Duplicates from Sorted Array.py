from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:]=(sorted(set(nums)))
        return len(nums)
if __name__=="__main__":
    obj=Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    result=obj.removeDuplicates(nums)
    print(result)
           
