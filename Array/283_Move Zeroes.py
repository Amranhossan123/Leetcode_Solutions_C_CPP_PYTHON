from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos=0
        for i in range(len(nums)):
            if(nums[i]==0):
                continue
            else:
                nums[pos]=nums[i]
                pos=pos+1
        while pos<len(nums):
            nums[pos]=0
            pos=pos+1
        print(nums)
sol=Solution()        
num_list= [0,1,0,3,12]
sol.moveZeroes(num_list)


        