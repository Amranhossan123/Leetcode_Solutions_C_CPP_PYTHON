from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        size1=len(list1)
        digit_t=list()
        word_t=list()
        for i in range(size1):
            if(list1[i] in list2):
                idx=list2.index(list1[i])
                t_sum=i+idx
                digit_t.append(t_sum)
                word_t.append(list1[i])
        min_sum=min(digit_t)
        result=list()
        for i in range(len(digit_t)):
            if(digit_t[i]==min_sum):
                result.append(word_t[i])
        return result

if __name__=="__main__":
    sol=Solution()

    list1 = ["Shogun","Tapioca Express","Burger King","KFC"] 
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    result=list()
    result=sol.findRestaurant(list1,list2)
    print(result)



        
        
        