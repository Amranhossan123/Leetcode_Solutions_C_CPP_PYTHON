from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        result_list=list()
        for i in range(n+1):
            count=0
            while(i>0):
                rem=i%2
                i=i//2
                if(rem==1):
                    count+=1
            result_list.append(count)
        return result_list
if __name__=="__main__":
    obj=Solution()
    n = 5
    result=obj.countBits(n)
    print(result)


        

        