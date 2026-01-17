class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:   
            total = 0
            for digit in str(num):
                total += int(digit)
            num = total
        return num


if __name__=="__main__":
    obj=Solution()
    num = 38
    result=obj.addDigits(num)
    print(result)
    