from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        limit=len(nums)
        for i in range(k):
            min_num=min(nums)
            min_idx=nums.index(min_num)
            nums[min_idx]=-nums[min_idx]
        total=0
        for i in range(limit):
            total+=nums[i]
        return total
    
if __name__=="__main__":
    obj=Solution()
    nums = [2,-3,-1,5,-4]
    k = 2
    result=obj.largestSumAfterKNegations(nums,k)
    print(result)

        
        