from typing import List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_dict=dict()
        for i in nums:
            if i in nums_dict:
                nums_dict[i]+=1
            else:
                nums_dict[i]=1
        flag=None
        for key in nums_dict.keys():
            if nums_dict[key]>1:
                flag=key
                break
        if flag!=None:
            return flag 
        
if __name__=="__main__":
    obj=Solution()
    nums = [5,1,5,2,5,3,5,4]
    result=obj.repeatedNTimes(nums)
    print(result)
            
        