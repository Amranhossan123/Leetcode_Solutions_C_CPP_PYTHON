
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = {}
        
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        
        n_times = n // 3
        new_list = list()
        
        for i in range(n):
            if count[nums[i]] > n_times:
                if nums[i] in new_list:
                    continue
                else:
                    new_list.append(nums[i])
        return new_list

ob1 = Solution()
my_list = [3, 2, 3, 1, 2, 2]
result = ob1.majorityElement(my_list)
print("Majority Elements:", result)