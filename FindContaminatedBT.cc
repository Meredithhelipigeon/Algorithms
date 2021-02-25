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
class FindElements {
    TreeNode * NewRoot;    
public:
    TreeNode * rebuild(TreeNode* n, int x){
        if(n->left != NULL){
            rebuild(n->left, 2*x+1);
        }
        if(n->right != NULL){
            rebuild(n->right, 2*x+2);
        }
        n->val = x;
        return n;
    }
    
    FindElements(TreeNode* root) {
        NewRoot = rebuild(root, 0);
    }
    
    bool findHelp(int t, TreeNode * cur){
        if(cur==NULL) return false;
        if(t<cur->val) return false;
        if(t==cur->val){
          return true;  
        } else {
            return (findHelp(t,cur->left)||(findHelp(t,cur->right)));
        }
    }
    
    bool find(int target) {
        return findHelp(target,NewRoot);
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */
