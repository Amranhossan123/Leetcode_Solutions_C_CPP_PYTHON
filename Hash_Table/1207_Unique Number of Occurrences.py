from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict=dict()
        for digit in arr:
            if digit in arr_dict:
                arr_dict[digit]+=1
            else:
                arr_dict[digit]=1
        dict_list=list()
        for value in arr_dict.values():
            dict_list.append(value)
        dict_list_size=len(dict_list)
        dict_set=set(dict_list)
        dict_set_size=len(dict_set)
        if(dict_list_size==dict_set_size):
            return True
        else:
            return False
        


if __name__=="__main__":
    obj=Solution()
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    result=obj.uniqueOccurrences(arr)
    print(result)