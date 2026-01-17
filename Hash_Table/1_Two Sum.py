from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List_item=list()
        total_element=len(nums)
        for i in range(total_element):
            for j in range(i+1,total_element):
                if(nums[i]+nums[j]==target):
                    List_item.append(i)
                    List_item.append(j)
                    return List_item
                
if __name__=="__main__":
    obj=Solution()
    nums = [2,7,11,15]
    target = 9
    result=obj.twoSum(nums,target)
    print(result)
    

        