from typing import List  

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in digits:
            number = number * 10 + i
        number = number + 1
        list_1 = [int(i) for i in str(number)]
        return list_1



if __name__ == "__main__":
    sol = Solution() 
    
    test_input = [1, 2, 3] 
    result = sol.plusOne(test_input) 
    
    print(f"Input: {test_input}")
    print(f"Output: {result}")