#include<bits/stdc++.h>
using namespace std;
class Solution {
    public:
        int mySqrt(int x) {
         int result= sqrt(x) ; 
         return result;
        }
    };

int main()
{
    Solution obj;
    int result=obj.mySqrt(8);
    cout<<result<<endl;
    return 0;
}