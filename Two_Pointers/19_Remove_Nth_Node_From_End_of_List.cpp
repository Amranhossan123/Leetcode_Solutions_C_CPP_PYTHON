#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) {
        val = x;
        next = NULL;
    }
};

class Solution {
public:
    int size_list(ListNode* head) {
        int count = 0;
        while (head != NULL) {
            count++;
            head = head->next;
        }
        return count;
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count1 = size_list(head);

        // If head node needs to be deleted
        if (count1 == n) {
            ListNode* temp = head;
            head = head->next;
            delete temp;
            return head;
        }

        ListNode* temp = head;

        for (int i = 0; i < count1 - n - 1; i++) {
            temp = temp->next;
        }

        ListNode* delete_node = temp->next;
        temp->next = temp->next->next;
        delete delete_node;

        return head;
    }
};

int main() {
    Solution obj;

    // Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    int n = 2; // remove 2nd node from end

    head = obj.removeNthFromEnd(head, n);

    // Print updated list
    ListNode* temp = head;
    while (temp != NULL) {
        cout << temp->val << " ";
        temp = temp->next;
    }

    return 0;
}
