#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int element_sum = (n * (n + 1)) / 2;
        int array_sum = 0;
        
        for(int i = 0; i < nums.size(); i++){
            array_sum = array_sum + nums[i];
        }
        
        return element_sum - array_sum;
    }
};

int main() {
    Solution sol;
    
    vector<int> myNums = {3, 0, 1}; 
    
    int result = sol.missingNumber(myNums);
    
    cout << "The missing number is: " << result << endl;

    return 0;
}