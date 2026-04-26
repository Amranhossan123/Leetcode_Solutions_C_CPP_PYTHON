class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result_list=[]
        word1_len=len(word1)
        word2_len=len(word2)
        i=0
        while(True):
            if(word1_len <=i and word2_len<=i):
                break
            elif(word1_len>i and word2_len>i):
                result_list.append(word1[i])
                result_list.append(word2[i])
                i=i+1
            elif(word1_len>i and word2_len<=i):
                result_list.append(word1[i])
                i=i+1
            elif(word1_len<=i and word2_len>i):
                result_list.append(word2[i])
                i=i+1
        
        return "".join(result_list)

if __name__=="__main__":
    obj=Solution()
    word1 = "abc"
    word2 = "pqr"
    result=obj.mergeAlternately(word1,word2)
    print(result)
