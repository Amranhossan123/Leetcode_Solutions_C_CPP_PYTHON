from typing import List
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_dict = dict()
        
        first_idx = dict()
        last_idx = dict()
        
        for i in range(len(nums)):
            digit = nums[i]
            
            if digit in nums_dict:
                nums_dict[digit] += 1
            else:
                nums_dict[digit] = 1
                first_idx[digit] = i
            last_idx[digit] = i
            
        degree = 0
        for count in nums_dict.values():
            if count > degree:
                degree = count
        ans = len(nums) 
        
        for digit in nums_dict:
            if nums_dict[digit] == degree:
                length = last_idx[digit] - first_idx[digit] + 1
                if length < ans:
                    ans = length
                    
        return ans
    
if __name__=="__main__":
    obj=Solution()
    nums = [1,2,2,3,1,4,2]
    result=obj.findShortestSubArray(nums)
    print(result)