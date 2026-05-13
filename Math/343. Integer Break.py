class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        product = 1
        
        while n > 4:
            product *= 3
            n -= 3
        
        return product * n
    
if __name__=="__main__":
    obj=Solution()
    n=10
    result=obj.integerBreak(n)
    print(result)