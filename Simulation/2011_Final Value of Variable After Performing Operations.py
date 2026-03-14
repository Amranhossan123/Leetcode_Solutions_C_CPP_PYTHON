from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        limit=len(operations)
        x=0
        for i in range(limit):
            if(operations[i]=="++X" or operations[i]=="X++"):
                x+=1
            elif(operations[i]=="--X" or operations[i]=="X--"):
                x-=1
        return x

if __name__=="__main__":
    obj=Solution()
    operations = ["X++","++X","--X","X--"]
    result=obj.finalValueAfterOperations(operations)
    print(result)