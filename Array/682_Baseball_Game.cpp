#include<bits/stdc++.h>
using namespace std;
class Solution {
    public:
        int calPoints(vector<string>& operations) {
            stack<int>st;
            for(string s:operations){
                if(s=="+"){
                    int prev1=st.top();
                    st.pop();
                    int prev2=st.top();
                    st.push(prev1);
                    st.push(prev1+prev2);
                }
                else if(s=="D"){
                    st.push(st.top()*2);
                }else if(s=="C"){
                    st.pop();
                }else{
                    st.push(stoi(s));
                }
            }
            int result=0;
            while(!st.empty()){
                result=result+st.top();
                st.pop();
            }
            return result;
        }
    };

int main()
{
    Solution s;
    vector<string>operations={"5","2","C","D","+"};
    cout<<s.calPoints(operations)<<endl;
    return 0;
}