from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = list()
        limit = len(nums1)
        for i in range(limit):
            if nums1[i] in nums2:
                nums3.append(nums1[i])
                nums2.remove(nums1[i])
        return nums3


if __name__ == "__main__":
    sol = Solution()
    
    
    list1 = [1, 2, 2, 1]
    list2 = [2, 2]
    result = sol.intersect(list1, list2)
    print(f"Intersection: {result}")