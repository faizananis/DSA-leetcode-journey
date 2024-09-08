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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        vector<ListNode*> res;
        ListNode* mainHead=head;
        ListNode* partHead=NULL;
        int size=0;
        ListNode* t=head;
        int div=0;
        int mod=-1;
        while(t!=NULL)
        {
            size++;
            t=t->next;
        }
        div=size/k;
        if(div!=0)
        {
            mod=size%k;
        }
        if(mod==-1)
        {
            while(k>0)
            {
                partHead=NULL;
                if(mainHead!=NULL)
                {
                    partHead=new ListNode();
                    partHead->val=mainHead->val;
                    mainHead=mainHead->next;
                }
                res.push_back(partHead);
                k--;
            }
        }
        else
        {
            int i=0;
            int j=0;
            int partLength=div;
            for(i=0;i<k;i++)
            {
                partHead=new ListNode();
                t=partHead;
                if(mod>0)
                {
                    partLength=div+1;
                    mod--;
                }
                else
                {
                    partLength=div;
                }
                for(j=0;j<partLength;j++)
                {
                    if(j>0)
                    {
                        t->next=new ListNode(mainHead->val);
                        t=t->next;
                    }
                    else
                    {
                        t->val=mainHead->val;
                    }
                    mainHead=mainHead->next;
                }
                res.push_back(partHead);
            }
        }
        return res;
    }
};