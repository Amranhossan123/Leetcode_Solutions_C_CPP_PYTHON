from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    
    my_list = [1, 1, 2, 2, 3, 4, 4]
    
    result_length = sol.removeDuplicates(my_list)
    
    print(f"New List Length:{result_length}")
    print(f"Updated List:{my_list}")