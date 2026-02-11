from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for taka in bills:
            if taka==5:
                five+=1
            elif taka==10:
                if five==0:
                    return False
                elif five>0:
                    five-=1
                    ten+=1
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
    
if __name__=="__main__":
    obj=Solution()
    bills = [5,5,5,10,20]
    result=obj.lemonadeChange(bills)
    print(result)
        