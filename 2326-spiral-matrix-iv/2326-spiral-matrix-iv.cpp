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
            // if(i==-1)
            // {
            //     i=0;
            //     lowi=true;
            // }
            // if(j==-1)
            // {
            //     j=0;
            //     lowj=true;
            // }
            // if(i==m)
            // {
            //     i=m-1;
            //     highi=true;
            // }
            // if(j==n)
            // {
            //     j=n-1;
            //     highj=true;
            // }
            // if(num%2==0)
            // {
            //     if(flag==false&&highj==false)
            //     {
            //         if(arr[i][j]!=-1)
            //         {
            //             flag=true;
            //         }
            //         else
            //         {
            //             y=j;
            //         }
            //         if(flag==false)
            //             j++;
            //         if(lowj==true)
            //             lowj=false;
            //     }
            //     else if(flag==true&&highi==false)
            //     {
            //         if(arr[i][j]!=-1)
            //         {
            //             flag=false;
            //         }
            //         else
            //         {
            //             x=i;
            //         }
            //         if(flag==true)
            //             i++;
            //         if(lowi==true)
            //             lowi=false;
            //     }
            //     else
            //     {
            //         num++;
            //     }
            // }
            // else
            // {
            //     if(flag==false&&lowj==false)
            //     {
            //         if(arr[i][j]!=-1)
            //         {
            //             flag=true;
            //         }
            //         else
            //         {
            //             y=j;
            //         }
            //         if(flag==false)
            //             j--;
            //         if(highj==true)
            //             highj=false;
            //     }
            //     else if(flag==true&&lowi==false)
            //     {
            //         if(arr[i][j]!=-1)
            //         {
            //             flag=false;
            //         }
            //         else
            //         {
            //             x=i;
            //         }
            //         if(flag==true)
            //             i--;
            //         if(highi==true)
            //             highi=false;
            //     }
            //     else
            //     {
            //         num++;
            //     }
            // }
            // arr[x][y]=head->val;
            // head=head->next;
           
            // if(j<n-num&&j>=num-1)
            // {
            //     if(n%2==0)
            //         j++;
            //     else
            //         j--;
            //     pos=j;
            // }
            // else if(i<m-num&&i>=num)
            // {
            //     if(num%2==0)
            //         i++;
            //     else
            //         i--;
            //     pos=i;
            // }
            // else
            // {
            //     num++;
            //     if(j==-1)
            //     {
            //         j=nums;
            //     }
            //     if(i==-1)
            //     {
            //         i=nums;
            //     }
            // }
            

        }
        cout<<i;
        return arr;
    }
};