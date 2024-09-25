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
        ListNode *temp=head->next;
        ListNode *tempSum=head->next;
        while(temp)
        {
            if(temp->val==0)
            {
                tempSum->next=temp->next;
                tempSum=tempSum->next;
            }
            else
            {
                tempSum->val=tempSum->val + temp->next->val;
            }
            temp=temp->next;
        }
        return head->next;
    }
};