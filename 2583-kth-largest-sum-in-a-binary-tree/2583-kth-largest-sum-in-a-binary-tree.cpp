/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    #define ll long long
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        priority_queue<ll,vector<ll>,greater<ll>> minheap;
        queue<TreeNode*> q;
        q.push(root);
        ll sum_of_level=0;
        int size=q.size();
        TreeNode *curr=NULL;
        while(q.empty()==0)
        {
            sum_of_level = 0;
            size = q.size();
            for(int i=0;i<size;i++)
            {
                curr = q.front();
                q.pop();
                sum_of_level += curr->val;
                if(curr->left!=NULL)
                {
                    q.push(curr->left);
                }
                if(curr->right!=NULL)
                {
                    q.push(curr->right);
                }
            }
            minheap.push(sum_of_level);
            if(minheap.size()>k)
            {
                minheap.pop();
            }
        }
        if(minheap.size() < k)
        {
            return -1;
        }
        return minheap.top();
    }
};