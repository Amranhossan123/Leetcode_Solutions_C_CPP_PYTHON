#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* fast = head;
        ListNode* slow = head;
        int flag = 0;
        
        while(fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if(fast == slow) {
                flag = 1;
                break;
            }
        }
        
        return flag == 1;
    }
};

int main() {
    ListNode* head = new ListNode(3);
    ListNode* second = new ListNode(2);
    ListNode* third = new ListNode(0);
    ListNode* fourth = new ListNode(-4);

    head->next = second;
    second->next = third;
    third->next = fourth;
    
    fourth->next = second; 

    Solution sol;
    if (sol.hasCycle(head)) {
        cout << "Cycle Detected!" << endl;
    } else {
        cout << "No Cycle Found." << endl;
    }

    return 0;
}