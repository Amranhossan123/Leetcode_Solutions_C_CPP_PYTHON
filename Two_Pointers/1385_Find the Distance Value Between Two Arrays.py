from typing import List
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        limit1=len(arr1)
        limit2=len(arr2)
        count=0
        for i in range(limit1):
            flag=True
            for j in range(limit2):
                if(abs(arr1[i]-arr2[j])<=d):
                    flag=False
                    break

            if(flag==True):
                count+=1
        return count
                    
if __name__=="__main__":
    obj=Solution()
    arr1 = [4,5,8] 
    arr2 = [10,9,1,8] 
    d = 2
    result=obj.findTheDistanceValue(arr1,arr2,d)
    print(result)