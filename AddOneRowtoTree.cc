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
    void FindUpperN(TreeNode* current, int depth, int aim, int v){
        if(current == NULL) return;
        // aim is N-1
        if(depth==aim){
            TreeNode* leftTree= new TreeNode(v,current->left,NULL);
            TreeNode* rightTree=new TreeNode(v,NULL,current->right);
            current->left=leftTree;
            current->right=rightTree;
        } else {
            FindUpperN(current->left, depth+1, aim, v);
            FindUpperN(current->right, depth+1, aim, v);
        }
    }
    
    
    
    
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if(root==NULL) root = new TreeNode(v);
        if(d==1){
            root = new TreeNode(v,root, NULL);
        } else {
            FindUpperN(root,1,d-1,v);
        }
        return root;
    }
};
