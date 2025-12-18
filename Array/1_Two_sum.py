from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        total = len(nums)
        for i in range(total):
            for j in range(i + 1, total):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result


if __name__ == "__main__":
    obj = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    print(obj.twoSum(nums, target))
