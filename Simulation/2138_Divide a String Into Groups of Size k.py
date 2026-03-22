from typing import List
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result_list=[]
        for i in range(0,len(s),k):
            crope=s[i:i+k]
            if len(crope) < k:
                need=k-len(crope)
                crope=crope+(fill *need)
            result_list.append(crope)
        return result_list

if __name__=="__main__":
    obj=Solution()
    s = "abcdefghij"
    k = 3
    fill = "x"
    result=obj.divideString(s,k,fill)
    print(result)

        