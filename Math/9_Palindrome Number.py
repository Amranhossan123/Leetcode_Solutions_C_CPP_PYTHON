class Solution:
    def isPalindrome(self, x: int) -> bool:
        real_num=x
        sum_of_num=0
        while(x>0):
            sum_of_num=10*(sum_of_num)+x%10
            x=x//10
        if(real_num==sum_of_num):
            return True
        else:
            return False

if __name__=="__main__":
    obj=Solution()
    x = 121
    result=obj.isPalindrome(x)
    print(result)