from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        limit=len(nums)
        for i in range(limit):
            for j in range(i+1,limit):
                if (nums[i]>nums[j]):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        print(nums)

if __name__=="__main__":
    obj=Solution()
    nums = [2,0,2,1,1,0]
    obj.sortColors(nums)
    
        