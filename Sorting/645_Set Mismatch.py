from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        limit=len(nums)
        result_list=list()
        nums_dict=dict()
        for digit in nums:
            if digit in nums_dict:
                nums_dict[digit]+=1
            else:
                nums_dict[digit]=1
        
        for i in range(1,limit+1):
            if i in nums_dict and nums_dict[i]>1:
                result_list.append(i)
        for i in range(1,limit+1):
            if i not in nums_dict:
                result_list.append(i)
        return result_list
    
if __name__=="__main__":
    obj=Solution()
    nums = [1,2,2,4]
    result=obj.findErrorNums(nums)
    print(result)

        

        