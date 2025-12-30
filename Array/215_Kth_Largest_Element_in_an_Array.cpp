#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end(), greater<int>());
        int result = nums[k - 1];
        return result;
    }
};

int main() {
    Solution sol;
    
    vector<int> nums = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    int k = 4;

    int output = sol.findKthLargest(nums, k);

    cout << "The " << k << "-th largest element is: " << output << endl;

    return 0;
}