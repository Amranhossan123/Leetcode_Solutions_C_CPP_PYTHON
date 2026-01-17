#include<bits/stdc++.h>
using namespace std;
class Solution {
    public:
        bool isValid(string s) {
            stack<char>st;
            for(char c:s){
                if(c=='(' || c=='{'  || c=='['){
                    st.push(c);
                }else{
                    if(st.empty()==true){
                        return false;
                    }else if(c==')' && st.top()=='('){
                        st.pop();
                    }
                    else if(c=='}' && st.top()=='{'){
                        st.pop();
                    }
                    else if(c==']' && st.top()=='['){
                        st.pop();
                    }
                    else{
                        return false;
                    }
                }
                
            }
            if(st.empty()==true){
                return true;
            }else{
                return false;
            }
        }
    };

int main()
{
    Solution obj;
    string s = "([)]";
    bool result;
    result=obj.isValid(s);
    cout<<result<<endl;
    return 0;
}