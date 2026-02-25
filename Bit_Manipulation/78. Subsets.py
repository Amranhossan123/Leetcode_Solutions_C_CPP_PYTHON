from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_len=len(nums)
        limit=pow(2,nums_len)
        result_list=list()
        for i in range(limit):
            nums_list=list()
            for j in range(nums_len):
                if(i>>j)&1:
                    nums_list.append(nums[j])
            result_list.append(nums_list)
        return result_list
    
if __name__=="__main__":
    obj=Solution()
    nums = [1,2,3]
    result=obj.subsets(nums)
    print(result)


        