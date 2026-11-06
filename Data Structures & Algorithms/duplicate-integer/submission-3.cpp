class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
     std::set<int> seen;

     for (int num:nums)
     {
        if (!seen.contains(num))
        {
            seen.insert(num);
            continue;
        }
        return true;

     }
     return false;   
    }
};