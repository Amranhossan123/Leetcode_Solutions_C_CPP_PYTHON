from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_list = list()
        new_set = set(nums)
        size_set = len(nums)
        for i in range(1, size_set + 1):
            if i not in new_set:
                new_list.append(i)
        return new_list
if __name__ == "__main__":
    sol = Solution()
    
    test_nums = [4, 3, 2, 7, 8, 2, 3, 1]
    
    result = sol.findDisappearedNumbers(test_nums)
    
    print(f"ইনপুট লিস্ট: {test_nums}")
    print(f"হারিয়ে যাওয়া সংখ্যাগুলো: {result}")