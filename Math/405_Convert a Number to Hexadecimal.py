class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if num<0:
            num=num & 0xFFFFFFFF
        result=list()
        digit_chars="0123456789abcdef"
        while(num>0):
            reminder=num%16
            result.append(digit_chars[reminder])
            num=num//16
        result.reverse()
        return "".join(result)

if __name__=="__main__":
    obj=Solution()
    num = -1
    result=obj.toHex(num)
    print(result)


            
        