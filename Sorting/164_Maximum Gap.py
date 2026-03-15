from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        limit=len(nums)
        different_list=[]
        nums.sort()
        if limit<2:
            return 0
        for i in range(limit-1):
            diff=abs(nums[i]-nums[i+1])
            different_list.append(diff)
        return max(different_list)
        
if __name__=="__main__":
    obj=Solution()
    nums = [3,6,9,1]
    result=obj.maximumGap(nums)
    print(result)