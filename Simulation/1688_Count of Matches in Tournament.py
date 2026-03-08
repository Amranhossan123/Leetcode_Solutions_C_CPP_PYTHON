class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_match=0
        teams=n
        while(teams>1):
            if(teams%2==0):
                matches=teams//2
                total_match+=matches
                teams=teams//2
            elif(teams%2!=0):
                matches=(teams-1)//2
                total_match+=matches
                teams=(teams-1)//2+1
        return total_match



if __name__=="__main__":
    obj=Solution()
    n = 7
    result=obj.numberOfMatches(n)
    print(result)