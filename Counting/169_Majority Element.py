from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
    
if __name__=="__main__":
    obj=Solution()
    nums = [2,2,1,1,1,2,2]
    result=obj.majorityElement(nums)
    print(result)
