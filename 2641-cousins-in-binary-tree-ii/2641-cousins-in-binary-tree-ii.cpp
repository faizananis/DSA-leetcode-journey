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
public:
    TreeNode* replaceValueInTree(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        TreeNode *curr=NULL;
        int size=0;
        int curr_level_sum=root->val;
        int next_level_sum=0;
        int sibling_sum=0;
        while(q.empty()==0)
        {
            size = q.size();
            next_level_sum=0;
            sibling_sum=0;
            for(int i=0;i<size;i++)
            {
                curr=q.front();
                q.pop();

                curr->val=curr_level_sum - curr->val;
                sibling_sum = (curr->left?curr->left->val:0)+(curr->right?curr->right->val:0);
                next_level_sum+=sibling_sum;

                if(curr->left)
                {
                    curr->left->val = sibling_sum;
                    q.push(curr->left);
                }
                if(curr->right)
                {
                    curr->right->val=sibling_sum;
                    q.push(curr->right);
                }
            }
            curr_level_sum = next_level_sum;
        }
        return root;
    }
};