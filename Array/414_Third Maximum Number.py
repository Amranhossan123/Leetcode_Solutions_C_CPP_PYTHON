from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
            max1=max(nums)
            while max1 in nums:
                nums.remove(max1)
            if not nums:
                return max1
            max2=max(nums)
            while max2 in nums:
                nums.remove(max2)
            if not nums:
                return max1
            max3=max(nums)
            return max3

if __name__=="__main__":
    sol=Solution()
    nums = [3,2,1]
    print(sol.thirdMax(nums))


        