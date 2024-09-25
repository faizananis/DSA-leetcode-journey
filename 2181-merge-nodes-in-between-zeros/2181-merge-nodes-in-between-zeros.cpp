/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        int sum = 0;
        ListNode* temp = head->next;
        ListNode* ans = new ListNode(-1);
        ListNode* tempAns = ans;
        while (temp) {
            if (temp->val != 0) {
                sum += temp->val;
            } else {
                ListNode* newnode = new ListNode(sum);
                sum = 0;
                tempAns->next = newnode;
                tempAns = tempAns->next;
            }
            temp = temp->next;
        }
        return ans->next;
    }
};