class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if divisor == 0:
            return INT_MAX
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            while dividend >= temp << 1:
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            result += multiple
        
        result *= sign
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result

if __name__=="__main__":
    obj=Solution()
    dividend = 10
    divisor = 3
    result=obj.divide(dividend,divisor)
    print(result)