from typing import  List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        first_char=letters[0]
        letters.sort()
        for char in letters:
            if char>target:
                return char
        return first_char
    
if __name__=="__main__":
    obj=Solution()
    letters = ["x","x","y","y"]
    target = "z"
    result=obj.nextGreatestLetter(letters,target)
    print(result)

        