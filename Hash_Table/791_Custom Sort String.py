class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        result = ""
        for char in order:
            if char in char_count:
                result += char * char_count[char]
                del char_count[char]
        for char in char_count:
            result += char * char_count[char]
            
        return result
        
if __name__=="__main__":
    obj=Solution()
    order = "bcafg"
    s = "abcd"
    result=obj.customSortString(order,s)
    print(result)