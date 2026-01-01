from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        khata = {} 
        
        for index in range(len(nums)):
            shonkha = nums[index] 
            
            if shonkha in khata:
                gap = index - khata[shonkha]
                if gap <= k:
                    return True 
            
            khata[shonkha] = index
            
        return False

sol = Solution()
test_nums = [1, 2, 3, 1, 2, 3]
k_value = 2

result = sol.containsNearbyDuplicate(test_nums, k_value)
print(f"Result : {result}") 