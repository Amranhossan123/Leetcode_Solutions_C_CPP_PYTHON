from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0
        i = 0   
        j = 0   

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count

if __name__=="__main__":
    sol=Solution()
    g = [1,2,3] 
    s = [1,1]
    result=sol.findContentChildren(g,s)
    print(result)

        