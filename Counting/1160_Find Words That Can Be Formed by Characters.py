from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total=0
        for word in words:
            is_form=True
            for char in word:
                if word.count(char)>chars.count(char):
                    is_form=False
                    break
            if is_form:
                total+=len(word)
                
        return total
    
if __name__=="__main__":
    obj=Solution()
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    result=obj.countCharacters(words,chars)
    print(result)

                
        