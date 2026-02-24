from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_list=s1.split()
        s2_list=s2.split()
        s1_dict=dict()
        s2_dict=dict()
        for word in s1_list:
            if word in s1_dict:
                s1_dict[word]+=1
            else:
                s1_dict[word]=1
        for word in s2_list:
            if word in s2_dict:
                s2_dict[word]+=1
            else:
                s2_dict[word]=1
        
        result_list=[]
        for key,value in s1_dict.items():
            if key not in s2_dict and value==1:
                result_list.append(key) 
        for key,value in s2_dict.items():
            if key not in s1_dict and value==1:
                result_list.append(key)
        return result_list

if __name__=="__main__":
    obj=Solution()
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    result=obj.uncommonFromSentences(s1,s2)
    print(result)