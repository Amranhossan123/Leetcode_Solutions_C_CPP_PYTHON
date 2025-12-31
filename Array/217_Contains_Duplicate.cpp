#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if(nums.empty()) return false;
        int flag = 0;
        map<int, int> mp;
        for(auto it = nums.begin(); it != nums.end(); it++) {
            mp[*it]++;
            if(mp[*it] > 1) {
                flag = 1;
                break;
            }
        }
        if(flag == 0) return false;
        else return true;
    }
};

int main() {
    Solution sol;
    
    vector<int> input = {1, 2, 3, 1}; 
    
    if(sol.containsDuplicate(input)) {
        cout << "True (Duplicate found)" << endl;
    } else {
        cout << "False (No duplicate)" << endl;
    }

    return 0;
}