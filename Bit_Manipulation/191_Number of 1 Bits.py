class Solution:
    def hammingWeight(self, n: int) -> int:
        result_list=list()
        while(n>0):
            bit=n%2
            result_list.append(bit)
            n=n//2
        limit=len(result_list)
        count=0
        for i in range(limit):
            if(result_list[i]==1):
                count+=1
        return count

if __name__=="__main__":
    obj=Solution()
    n = 11
    result=obj.hammingWeight(n)
    print(result)