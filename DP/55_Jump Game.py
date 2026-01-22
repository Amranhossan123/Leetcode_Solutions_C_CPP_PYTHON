from typing import List
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        n = len(nums)
        
        for i in range(n):
            if i > max_reach:
                return False
            
            if i + nums[i] > max_reach:
                max_reach = i + nums[i]
            
            if max_reach >= n - 1:
                return True
                
        return False
    
if __name__=="__main__":
    obj=Solution()
    nums = [2,3,1,1,4]
    result=obj.canJump(nums)
    print(result)