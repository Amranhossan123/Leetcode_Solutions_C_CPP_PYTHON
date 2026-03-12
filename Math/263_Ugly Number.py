class Solution:
    def isUgly(self, n: int) -> bool:
        if(n==1):
            return True
        if(n<=0):
            return False
        for factory in [2,3,5]:
            while n%factory==0:
                n=n//factory
        
        return n==1
        
if __name__=="__main__":
    obj=Solution()
    n = 6
    result=obj.isUgly(n)
    print(result)