from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        limit=len(nums)
        result=0
        current=0
        if(limit<3):
            return 0
        for i in range(2,limit):
            if(nums[i]-nums[i-1]==nums[i-1]-nums[i-2]):
                current+=1
                result+=current
            else:
                current=0
        return result

if __name__=="__main__":
    sol=Solution()
    list1=[1,2,3,4]
    print(sol.numberOfArithmeticSlices(list1))

        