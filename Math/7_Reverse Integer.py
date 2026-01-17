class Solution:
    def reverse(self, x: int) -> int:
        max_x=2**31-1
        min_x=-2**31
        original_x=x
        abs_x=abs(x)
        reverse_x=0
        if(original_x >= max_x or original_x <= min_x):
            return 0
        while(abs_x > 0):
            reverse_x= reverse_x * 10 + (abs_x % 10)
            abs_x=abs_x // 10
        if(original_x < 0):
            reverse_x=-reverse_x
        if(reverse_x > max_x or reverse_x < min_x):
            return 0
        return reverse_x
        

if __name__=="__main__":
    obj=Solution()
    x = 123
    result=obj.reverse(x)
    print(result)