from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result_list=list()
        limit1=len(nums1)
        limit2=len(nums2)
        for i in range(limit1):
            position=nums2.index(nums1[i])
            temp=False
            for j in range(position,limit2):
                if(nums1[i] <nums2[j]):
                    temp=True
                    result_list.append(nums2[j])
                    break
            if(temp==False):
                result_list.append(-1)
        return result_list
                
if __name__=="__main__":
    obj=Solution()
    nums1 = [4,1,2] 
    nums2 = [1,3,4,2]
    result=obj.nextGreaterElement(nums1,nums2)
    print(result)


        