from typing import List
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        deck_dict = {}
        for card in deck:
            if card in deck_dict:
                deck_dict[card] += 1
            else:
                deck_dict[card] = 1
        counts = list(deck_dict.values())
        
        min_count = min(counts)
        
        for x in range(2, min_count + 1):
            possible = True
            for count in counts:
                if count % x != 0:
                    possible = False
                    break
            
            if possible:
                return True
                
        return False
    
if __name__=="__main__":
    obj=Solution()
    deck = [1,1,1,2,2,2,3,3]
    result=obj.hasGroupsSizeX(deck)
    print(result)