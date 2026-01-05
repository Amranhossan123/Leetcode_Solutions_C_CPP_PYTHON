from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.add(nums1[i])
        return list(result)

sol = Solution()

list1 = [1, 2, 2, 1]
list2 = [2, 2]
print(sol.intersection(list1, list2))
