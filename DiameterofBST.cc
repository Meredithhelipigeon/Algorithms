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
    int MaxDepth(TreeNode* root){
        if(root==NULL){
            return 0;
        } else {
            return 1+max(MaxDepth(root->left),MaxDepth(root->right));
        }
    }
    
    int diameterOfBinaryTree(TreeNode* root) {
        if (root==NULL){
            return 0;
        } else {
            cout <<  MaxDepth(root->left) << " " << MaxDepth(root->right) <<  endl;
            return max(MaxDepth(root->left)+MaxDepth(root->right), max(diameterOfBinaryTree(root->left), diameterOfBinaryTree(root->right)));
        }
    }
};
