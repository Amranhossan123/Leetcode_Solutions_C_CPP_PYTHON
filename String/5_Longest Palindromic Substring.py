class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            word1 = self.check(s, i, i)
            word2 = self.check(s, i, i + 1)
            res = max(res, word1, word2, key=len)
        return res
    def check(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

if __name__=="__main__":
    obj=Solution()
    s = "babad"
    result=obj.longestPalindrome(s)
    print(result)