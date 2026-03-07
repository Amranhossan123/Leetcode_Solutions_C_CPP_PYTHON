from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p=[]
        for i in range(1,m+1):
            p.append(i)
        result=[]
        for digit in queries:
            if digit in p:
                q_index=p.index(digit)
                result.append(q_index)
                p.remove(digit)
                p.insert(0,digit)
        return result
    
if __name__=="__main__":
    obj=Solution()
    queries = [7,5,5,8,3]
    m = 8
    result=obj.processQueries(queries,m)
    print(result)