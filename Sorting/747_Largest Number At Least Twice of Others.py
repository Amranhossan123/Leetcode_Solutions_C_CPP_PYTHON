from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums2=list(nums)
        nums.sort()
        limit=len(nums)
        max1=nums[limit-1]
        max2=nums[limit-2]
        if(max2*2<=max1):
            return nums2.index(max1)
        return -1
        
if __name__=="__main__":
    obj=Solution()
    nums = [3,6,1,0]
    result=obj.dominantIndex(nums)
    print(result)