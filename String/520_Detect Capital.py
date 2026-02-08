class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        limit=len(word)
        count=0
        for char in word:
            if char.isupper():
                count+=1
        if(count==0 or count==limit):
            return True
        if(count==1 and word[0].isupper()):
            return True
        return False

if __name__=="__main__"        :
    obj=Solution()
    word = "USA"
    result=obj.detectCapitalUse(word)
    print(result)
            



        