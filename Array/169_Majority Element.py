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

sol = Solution()
my_list = [2, 2, 1, 1, 1, 2, 2] 
result = sol.majorityElement(my_list)

print(f"The majority element is: {result}")