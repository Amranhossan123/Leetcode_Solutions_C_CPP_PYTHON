from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        limit=len(arr)
        count=0
        for i in range(limit):
            for j in range(i+1,limit):
                for k in range(j+1,limit):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k]) <=c:
                        count+=1
        return count
    
if __name__=="__main__":
    obj=Solution()
    arr = [3,0,1,1,9,7]
    a = 7 
    b = 2 
    c = 3
    result=obj.countGoodTriplets(arr,a,b,c)
    print(result)

                    

        