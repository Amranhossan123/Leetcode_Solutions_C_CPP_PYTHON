from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            flag=1
            word_len=len(word)
            i=0
            j=word_len-1
            while(j>=i):
                if word[i]!=word[j]:
                    flag=0
                    break
                i+=1
                j-=1
            if(flag==1):
                return word
        return ""

if __name__=="__main__":
    obj=Solution()
    words = ["abc","car","ada","racecar","cool"]
    result=obj.firstPalindrome(words)
    print(result)
    