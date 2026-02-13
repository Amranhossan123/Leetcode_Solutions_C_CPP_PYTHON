from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score=sorted(score,reverse=True)
        rank=dict()
        for i in range(len(sorted_score)):
            if i==0:
                rank[sorted_score[i]]="Gold Medal"
            elif i==1:
                rank[sorted_score[i]]="Silver Medal"
            elif i==2:
                rank[sorted_score[i]]="Bronze Medal"
            else:
                rank[sorted_score[i]]=str(i+1)
        result_list=list()
        for i in score:
            result_list.append(rank[i])
        return result_list

if __name__=="__main__":
    obj=Solution()
    score = [10,3,8,9,4]
    result=obj.findRelativeRanks(score)
    print(result)
            

        