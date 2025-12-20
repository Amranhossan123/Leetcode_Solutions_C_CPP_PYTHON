from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

if __name__ == "__main__":
    sol = Solution()
    
    test_nums = [3, 2, 2, 3]
    val_to_remove = 3
    
    new_length = sol.removeElement(test_nums, val_to_remove)
    
    print(f"New Length (k): {new_length}")
    print(f"Changing List: {test_nums[:new_length]}")
    print(f"All List: {test_nums}")