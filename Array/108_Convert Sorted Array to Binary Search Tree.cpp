#include <iostream>
#include <vector>

using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* convert_binary(vector<int>& nums, int l, int r) {
        if (l > r) return NULL;
        
        int mid = l + (r - l) / 2; 
        TreeNode* root = new TreeNode(nums[mid]);
        
        root->left = convert_binary(nums, l, mid - 1);
        root->right = convert_binary(nums, mid + 1, r);

        return root;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return convert_binary(nums, 0, nums.size() - 1);
    }
};

void printInorder(TreeNode* node) {
    if (node == NULL) return;
    printInorder(node->left);
    cout << node->val << " ";
    printInorder(node->right);
}

int main() {
    Solution sol;
    
    vector<int> nums = {-10, -3, 0, 5, 9};

    TreeNode* root = sol.sortedArrayToBST(nums);

    cout << "BST Inorder Traversal: ";
    printInorder(root);
    cout << endl;

    return 0;
}