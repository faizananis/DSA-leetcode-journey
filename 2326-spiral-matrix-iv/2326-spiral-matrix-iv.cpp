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
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> arr(m,vector<int> (n,-1));
        int i=0;
        int j=0;
        int num=0;
        while(head)
        {
            for(j=num;j<n;j++)
            {
                if(arr[i][j]!=-1||head==NULL)
                {
                    break;
                }
                arr[i][j]=head->val;
                head=head->next;
            }
            if(head==NULL)
            {
                break;
            }
            j--;
            for(i=num+1;i<m;i++)
            {
                if(arr[i][j]!=-1||head==NULL)
                {
                    break;
                }
                arr[i][j]=head->val;
                head=head->next;
            }
            if(head==NULL)
            {
                break;
            }
            i--;
            for(j=n-num-2;j>=0;j--)
            {
                if(arr[i][j]!=-1||head==NULL)
                {
                    break;
                }
                arr[i][j]=head->val;
                head=head->next;
            }
            if(head==NULL)
            {
                break;
            }
            j++;
            for(i=m-num-2;i>=0;i--)
            {
                if(arr[i][j]!=-1||head==NULL)
                {
                    break;
                }
                arr[i][j]=head->val;
                head=head->next;
            }
            if(head==NULL)
            {
                break;
            }
            i++;
            num++;
        }
        cout<<i;
        return arr;
    }
};