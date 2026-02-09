from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_dict=dict()
        limit=len(arr1)
        temp_list=list()
        result_list=list()
        for i in arr1:
            if i in  arr1_dict:
                arr1_dict[i]+=1
            else:
                arr1_dict[i]=1
        for i in arr1:
            if i not in arr2:
                temp_list.append(i)
        temp_list.sort()
        for i in arr2:
            if i in arr1_dict:
                result_list.extend([i]*arr1_dict[i])
                del arr1_dict[i]
        return result_list+temp_list

if __name__=="__main__":
    obj=Solution()
    arr1 = [2,3,1,3,2,4,6,7,9,2,19] 
    arr2 = [2,1,4,3,9,6]
    result=obj.relativeSortArray(arr1,arr2)
    print(result)


        