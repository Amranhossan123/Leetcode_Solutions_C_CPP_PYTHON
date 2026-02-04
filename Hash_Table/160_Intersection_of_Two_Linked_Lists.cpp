#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL) return NULL;

        ListNode* temp = headA;
        ListNode* temp1 = headB;

        while (temp != temp1) {

            temp = (temp == NULL) ? headB : temp->next;
            temp1 = (temp1 == NULL) ? headA : temp1->next;
        }
        return temp; 
    }
};

int main() {
    ListNode* common = new ListNode(8);
    common->next = new ListNode(4);
    common->next->next = new ListNode(5);
    ListNode* headA = new ListNode(4);
    headA->next = new ListNode(1);
    headA->next->next = common;

    ListNode* headB = new ListNode(5);
    headB->next = new ListNode(6);
    headB->next->next = new ListNode(1);
    headB->next->next->next = common;

    Solution sol;
    ListNode* result = sol.getIntersectionNode(headA, headB);

    if (result) {
        cout << "Intersection point value: " << result->val << endl;
    } else {
        cout << "No intersection found." << endl;
    }

    return 0;
}