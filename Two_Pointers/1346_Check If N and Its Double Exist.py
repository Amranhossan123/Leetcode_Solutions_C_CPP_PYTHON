from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        limit=len(arr)
        for i in range(limit):
            for j in range(limit):
                if arr[i]==arr[j]*2 and i!=j:
                    return True
        return False
if __name__=="__main__":
    obj=Solution()
    arr = [3,1,7,11]
    result=obj.checkIfExist(arr)
    print(result)

        