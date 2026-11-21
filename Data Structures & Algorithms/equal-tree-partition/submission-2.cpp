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
private:
    vector<int> sums;
public:
    bool checkEqualTree(TreeNode* root) {
        if (!root) return root; 
        
        int total {sum(root)};
        sums.pop_back();
        for (int t:sums)
        {
            if (2*t == total) return true;

        }
        return false; 
        
        

    }
    int sum(TreeNode* root) 
    {
        if (!root) return 0;
        int s=root->val; 
        s += sum(root->left);
        s += sum(root->right);
        sums.push_back(s); 

        return s; 

    }
};
