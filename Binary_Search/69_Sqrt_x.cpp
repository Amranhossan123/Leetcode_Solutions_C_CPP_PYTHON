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
    int x = 8;
    Solution obj;
    int result=obj.mySqrt(x);
    cout<<result<<endl;
    return 0;
}