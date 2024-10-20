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
    ListNode* deleteMiddle(ListNode* head) {
        int i=0;
        int middle=0;
        ListNode *temp=head;
        ListNode *curr=NULL;
        if(head->next==NULL)
        {
            return NULL;
        }
        for(i=0;temp!=NULL;i++)
        {
            temp=temp->next;
        }
        middle=i/2;
        temp=head;
        for(i=0;i<middle-1;i++)
        {
            temp=temp->next;
        }
        curr=temp->next;
        temp->next=temp->next->next;
        curr->next=NULL;
        delete curr;
        return head;
    }
};