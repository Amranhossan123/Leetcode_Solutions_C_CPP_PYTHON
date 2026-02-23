class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        reverse_words=[]
        for word in s_list:
            reverse_word=word[::-1]
            reverse_words.append(reverse_word)
        return " ".join(reverse_words)



if __name__=="__main__":
    obj=Solution()
    s = "Let's take LeetCode contest"
    result=obj.reverseWords(s)
    print(result)