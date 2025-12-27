from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for item in nums:
            if item in seen:
                seen.remove(item)
            else:
                seen.add(item)
        return seen.pop()
if __name__ =="__main__":
    sol=Solution()
    test_nums = [4, 1, 2, 1, 2]
    result=sol.singleNumber(test_nums)
    print(f"The single number is: {result}")

