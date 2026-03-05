class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list=list(s)
        s_len=len(s_list)
        if(s_len < k):
            s_list.reverse()
        elif(s_len >=k and s_len <(2*k)):
            i=0
            j=k-1
            while(j>i):
                temp=s_list[i]
                s_list[i]=s_list[j]
                s_list[j]=temp
                i+=1
                j-=1
        elif(s_len >=(2*k)):
            for start in range(0,s_len-1,2*k):
                i=start
                j=min(start+k-1,s_len-1)
                while j>i:
                    s_list[i],s_list[j]=s_list[j],s_list[i]
                    i+=1
                    j-=1
        
        return "".join(s_list)
    
if __name__=="__main__":
    obj=Solution()
    s = "abcdefg"
    k = 2
    result=obj.reverseStr(s,k)
    print(result)

                




                
                

            
        