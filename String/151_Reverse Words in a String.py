from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        s_list.reverse()
        return " ".join(s_list)
    
if __name__=="__main__":
    obj=Solution()
    s = "the sky is blue"
    result=obj.reverseWords(s)
    print(result)

        