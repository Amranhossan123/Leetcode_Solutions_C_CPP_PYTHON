class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_set = set()
        for char in s:
            if char in s_set:
                s_set.remove(char)
            else:
                s_set.add(char)
        odds = len(s_set)
        if odds > 0:
            return len(s) - odds + 1
        else:
            return len(s)
        
if __name__=="__main__":
    obj=Solution()
    s = "abccccdd"
    result=obj.longestPalindrome(s)
    print(result)