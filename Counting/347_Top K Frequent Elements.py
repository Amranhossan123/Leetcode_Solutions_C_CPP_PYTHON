from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_element={}
        result=list()
        limit=len(nums)
        for i in range(limit):
            if nums[i] in count_element:
                count_element[nums[i]]+=1
            else:
                count_element[nums[i]]=1
        for j in range(k):
            max_value=max(count_element,key=count_element.get)
            result.append(max_value)
            del count_element[max_value]
        return result
        
if __name__=="__main__":
    obj=Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    result=obj.topKFrequent(nums,k)
    print(result)